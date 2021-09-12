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
        component: () => import('@/views/goods/Goods.vue'),
        children: [
          {
            path: '/',
            components: {
              unused: () => import('@/views/goods/Unused.vue'),
              inUsing: () => import('@/views/goods/InUsing.vue'),
              usedUp: () => import('@/views/goods/UsedUp.vue'),
            }
          }
        ]
      },
      {
        path: '/sum',
        name: 'Summaries',
        component: () => import('@/views/summaries/Summaries.vue'),
      },
      {
        path: '/stat',
        name: 'Statistics',
        component: () => import('@/views/statistics/Statistics.vue'),
      },
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