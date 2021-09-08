### 引入font-awesome图标库

1. npm 安装

   ``````
   $ npm i --save @fortawesome/fontawesome-svg-core
   $ npm i --save @fortawesome/free-solid-svg-icons    //安装免费solid版图标
   $ npm i --save @fortawesome/vue-fontawesome@latest  //适用于vue2.x
   ``````

2. @/main.js中添加

   ``````
   import { library } from '@fortawesome/fontawesome-svg-core'
   import { faUserSecret } from '@fortawesome/free-solid-svg-icons'  //此处为按需加载示例
   import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
   
   library.add(faUserSecret)
   
   Vue.component('font-awesome-icon', FontAwesomeIcon)
   ``````

3. 使用方式(两种)

   ``````
   <!-- The solid style is implicit -->
   <font-awesome-icon icon="user-secret" />
   
   <!-- It's better to be explicit -->
   <!-- Don't forget to bind the property with ":" (we forget all the time!) -->
   <font-awesome-icon :icon="['fas', 'user-secret']" />
   ``````

   