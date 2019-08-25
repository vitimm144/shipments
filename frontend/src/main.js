import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import { CardPlugin, TablePlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueResource from 'vue-resource'

Vue.use(BootstrapVue)
Vue.use(CardPlugin)
Vue.use(TablePlugin)
Vue.use(VueResource)

new Vue({
  el: '#app',
  render: h => h(App)
})
