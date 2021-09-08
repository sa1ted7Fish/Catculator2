### 修改默认css样式

##### 问题

例如修改`el-footer`高度。`el-footer`高度在element组件中默认为60px，且优先级较高，普通方式无法覆盖。

##### 解决方案

1. 使用`el-footer`自带attribute: height。

2. 使用`!important`

例如

``````
.el-footer{
  height: 40px !important;   //提高指定样式的优先级，覆盖默认样式
}
``````

