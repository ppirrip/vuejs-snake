// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

// add mqtt support with Vue-mqtt (https://github.com/nik-zp/Vue-Mqtt)
import VueMqtt from 'vue-mqtt'

// TODO:
// This need to be factor out later
var url = 'wss://io.adafruit.com:443/mqtt/',
    username = 'ppirrip',
    aio_key = '2aca2c25b0374611b25b22a5fdfbcc3d',
    topic = username + '/feeds/aiidex.response',
    counter = 0;

Vue.use(VueMqtt, url, {username: username, password: aio_key})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
