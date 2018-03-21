<template>
  <div class="vue-container">
	  <div class="game-container" :class="{ gameOver : gameStatus === 'gameOver' }">
		  <div class="message" v-if="gameStatus === 'gameOver'">GAMEOVER</div>
      <div class="score">Score: {{score}}</div>
		  <div class="case" v-for="n in cases" :class='{ snake : snake.indexOf(n) !== -1, fruits : fruits.indexOf(n) !== -1 }'></div>
	  </div>
  </div>
</template>

<script>
export default {
  name: 'Snake',
  data () {
    return {
      msg: 'Welcome to Snake',
      register_key : 'down',
      w : 8,
      h : 8,
      s : 10,
      snake_start_size : 2,
      snake : [],
      fruits : [10, 20, 40],
      interval : '',
      gameStatus : 'gameOver',
      speed : 1,
      score: 0,
    }
  },
  computed : {
    cases () {
			var res = this.w * this.h;
			return res;
		}
  },
  methods : {
    changeGameSize (val) {
			document.documentElement.style.setProperty('--gameSize', val + 'px');
		},
    changeCaseSize (val) {
			document.documentElement.style.setProperty('--caseSize', val + 'px');		
		},
    setSizes (w, s) {
			this.w = w;
			this.h = w;
			this.s = s;
			this.changeGameSize(w*s)
			this.changeCaseSize(s)
		},
    initSnake () {
			this.snake = [];
			var start_head = (this.cases / 2)  - (this.w / 2);
			this.snake.push(start_head, start_head - 1);
		},
    move () {
			var dir = this.register_key;
			switch(dir) {
				 case 'right':
						if( (this.snake[0] + this.speed) % this.w === 1 ){
					  		return (this.snake[0] + this.speed) - this.w
						}else{
							return this.snake[0] + this.speed
						}
				 case 'left':
					  if( (this.snake[0] - this.speed) % this.w === 0 ){
					  		return (this.snake[0] - this.speed) + this.w
						}else{
							return this.snake[0] - this.speed
						}
				 case 'up':
						if( this.snake[0] - this.w < 0 ){
					  		return this.snake[0] - this.w + this.cases
						}else{
							return this.snake[0] - this.h
						}
				 case 'down':
						if( this.snake[0] + this.h > this.cases ){
					  		return this.snake[0] + this.h - this.cases
						}else{
							return this.snake[0] + this.h
						}
				 default:
					  return 0
			}
		},
    moveSnake() {
			if( this.snake.indexOf(this.snake[0], 1) !== -1 ){
				this.gameStatus = 'gameOver'
				return false
      }
      if (this.speed === 0) {
        return true
      }
			this.snake.unshift(this.move());
			if( this.fruits.indexOf(this.snake[0]) === -1 ){
        this.snake.splice(-1, 1);
			}else{
				this.fruits.splice(this.fruits.indexOf(this.snake[0]), 1)
			}
		},
    randomApple () {
			if(this.fruits.length < 3){
				var new_apple = this.snake[0];
				while(this.snake.indexOf(new_apple) !== -1){
					new_apple = Math.round(Math.random() * this.cases)
				}
        this.fruits.push(new_apple)
        this.score += 10
			}
		},
    gameTurn () {
			if( this.gameStatus === 'gameOver' ){
				this.gameEnded()
			}else if( this.gameStatus === 'paused' ){
				this.gamePaused()
			}else{
				this.moveSnake()
				this.randomApple()
			}
		},
    launchGame () {
			this.gameStatus = 'playing'
			this.setSizes(this.w, this.s)
			this.initSnake()
			var self = this
			this.interval = setInterval(function(){
				self.gameTurn()
			}, 300);
		},
    gameEnded () {
			console.log('dead')
			clearInterval(this.interval)
		}
  },
  mounted () {
    this.msg += ' mounted'
    this.launchGame();
    var self = this;
    window.addEventListener("keyup", function(e){
			if(e.keyCode === 37){
				self.register_key = 'left'
			}else if(e.keyCode === 38){
				self.register_key = 'up'
			}else if(e.keyCode === 39){
				self.register_key = 'right'
			}else if(e.keyCode === 40){
				self.register_key = 'down'
			}
			if(e.keyCode === 32 && self.gameStatus === 'gameOver'){
				console.log('bob')
				self.launchGame()
			}
		});
  }
}
</script>

<style scoped>
/* :root{
  --caseSize : 10px;
	--gameSize : 80px;
	--snakeColor : forestgreen;
} */

.vue-container {
  --caseSize : 40px;
	--gameSize : 320px;
	--snakeColor : forestgreen;  
  font-family: sans-serif;
}
.vue-container .game-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translatex(-50%) translatey(-50%);
  max-width: var(--gameSize);
  max-height: var(--gameSize);
  line-height: var(--caseSize);
}
.vue-container .game-container .message {
  position: absolute;
  top: 50%;
  left: 50%;
  word-wrap: nowrap;
  transform: translatex(-50%) translatey(-50%);
  font-size: 20px;
  font-weight: 900;
  text-shadow: 2px 2px 0 white, -2px 2px 0 white, 2px -2px 0 white, -2px -2px 0 white;
}
.vue-container .game-container .score {
  transform: translatex(0%) translatey(-50%);
  font-size: 20px;
  font-weight: 900;
  text-shadow: 2px 2px 0 white, -2px 2px 0 white, 2px -2px 0 white, -2px -2px 0 white;
}
.vue-container .game-container .case {
  width: var(--caseSize);
  height: var(--caseSize);
  background-color: lightgrey;
  display: inline-block;
  padding: 0px 0px 0px 0px;
  margin: -40px 0px 0px 0px;
  box-sizing: border-box;
  border: 1px solid white;
}
.vue-container .game-container .case.snake {
  background-color: var(--snakeColor);
}
.vue-container .game-container .case.fruits {
  background-color: red;
}
.vue-container .game-container.gameOver .case {
  background-color: black;
  opacity: 0.1;
}


</style>