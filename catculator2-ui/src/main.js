import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/css/fonts.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
    faHome,
    faMoneyCheck,
    faChartLine,
    faCog,
    faSignOutAlt,
    faInfo,
    faYenSign,
    faCalendarCheck,
    faPercent
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
    faHome,
    faMoneyCheck,
    faChartLine,
    faCog,
    faSignOutAlt,
    faInfo,
    faYenSign,
    faCalendarCheck,
    faPercent
)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false
Vue.use(ElementUI);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
