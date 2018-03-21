<template>
  <div id="app">
    <Snake></Snake>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld'
import Snake from './components/Snake'

export default {
  name: 'App',
  components: {
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
