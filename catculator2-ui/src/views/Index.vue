<template>
  <el-container>
    <el-aside width="60px"><SideBar></SideBar></el-aside>
    <el-container style="min-height: 100vh">
      <el-header><Header></Header></el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "@/components/SideBar";
import Header from "@/components/Header";

export default {
  name: "Index",
  components: {
    SideBar,
    Header,
  },
};
</script>

<style scoped>
.el-header, .el-footer {
  margin-left: 60px;
  padding: 0;
}

.el-aside {
  text-align: center;
  height: 100vh;
  position: fixed;
  overflow: hidden;
  box-shadow: 0 0 5px 2px #DDDDDD;
}

.el-main {
  background-color: #ffffff;
  margin-left: 60px;
  padding: 0;
}

</style>