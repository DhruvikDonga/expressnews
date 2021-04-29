  
import Vue from 'vue'
import Router from 'vue-router'
import login from './components/login'
import register from './components/register'
import logout from './components/logout'
import home from './components/Home'
import welcome from './components/welcome'
import Savednews from './components/Savednews'
import Categorynews from './components/Categorynews'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      meta:{
        requiresAuth:true
      }
    },
    {
      path: '/welcome',
      name: 'welcome',
      component: welcome,
     
      
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        requiresLogged: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: {
        requiresLogged: true
      }
    },
    {
      path: '/savednews',
      name: 'savednews',
      component:Savednews,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/categories',
      name: 'categories',
      component:Categorynews,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout,
      meta: {
        requiresAuth: true
      }
    }
  ]
})