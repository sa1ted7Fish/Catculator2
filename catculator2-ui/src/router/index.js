import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/views/Index.vue'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home',
    name: 'Index',
    component: Index,
    children: [
      {
        path: '/home',
        name: 'Home',
        component: Home
      },
      {
        path: '/gds',
        name: 'Goods',
        component: () => import('@/views/goods/goods')
      },
      {
        path: '/stat',
        name: 'Statistics',
        component: () => import('@/views/statistics/statistics'),
        children: [
          {
            path: '/',
            components: {

            }
          }
        ]
      }
    ]
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   component: () => import('../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router