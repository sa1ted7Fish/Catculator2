### el组件引入图片src无效

##### 问题

el组件引入图片src路径无效

``````
<el-image src="@/assets/logo.png"></el-image>
``````

##### 解决

使用`require()`引入图片

``````
<el-image :src="require('@/assets/logo.png')"></el-image>
``````

