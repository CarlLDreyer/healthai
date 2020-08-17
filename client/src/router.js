import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  root: '/',
  routes: [{
    name: 'Home',
    path: '/',
    component: () => import(/* webpackChunkName: 'Home' */ './views/Home'),
  }]

})

export default router
