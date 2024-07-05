import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import studentlogin from '../views/components/studentlogin.vue'
import teacherlogin from '../views/components/teacherlogin.vue'
import studenthomepage from '../views/components/studenthomepage.vue'
import teacherhomepage from '../views/components/teacherhomepage.vue'




const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/stlogin',
    name: 'stlogin',
    component: studentlogin
  },
  {
    path: '/tlogin',
    name: 'tlogin',
    component: teacherlogin
  },
  {
    path: '/stlogin/:id',
    name:'shome',
    component: studenthomepage
  },
  {
    path: '/tlogin/:id',
    name:'thome',
    component: teacherhomepage
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
