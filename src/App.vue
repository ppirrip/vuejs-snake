<template>
  <div id="app">
    <!-- img src="./assets/logo.png" -->
    <!-- HelloWorld/ -->
    <Snake></Snake>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld'
import Snake from './components/Snake'

export default {
  name: 'App',
  components: {
    //HelloWorld,
    Snake,
  }
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
