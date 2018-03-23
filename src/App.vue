<template>
  <div id="app">
    <Snake></Snake>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld'
import sweetalert from 'sweetalert';
import Snake from './components/Snake'

export default {
  name: 'App',
  components: {
    Snake,
  },
  mounted () {
    // might need to use wildcard here later ...
    this.$mqtt.subscribe('ppirrip/feeds/aiidex.command')
  },
  data() { 
    return {
      cmds: []
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
