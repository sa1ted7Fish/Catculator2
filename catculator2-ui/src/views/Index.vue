<template>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-container style="min-height: 100vh">
      <el-header>Header</el-header>
      <el-main>Main

      </el-main>
      <el-footer>Catculator2 ©2021 Created by TJSDD</el-footer>
    </el-container>
  </el-container>
</template>

<script>
export default {

};
</script>

<style scoped>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
  margin-left: 200px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
  height: 100vh;
  position: fixed;
  overflow: auto;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
  margin-left: 200px;
}

</style>