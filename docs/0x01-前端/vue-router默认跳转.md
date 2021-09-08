### vue-router默认跳转

###### 问题

登录后默认跳转至`/home`页

##### 解决方案

使用vue-router的`redirect`

``````
const routes = [
  {
    path: '/',            
    redirect: '/home',    //设置redirect后，访问/时就会跳转至/home
  }
 ]
``````

 