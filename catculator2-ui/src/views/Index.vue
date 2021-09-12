<template>
  <el-container>
    <el-header height="70px">
      <Header></Header>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
import Header from "@/components/Header";

export default {
  name: "Index",
  components: {
    Header,
  },
};
</script>

<style scoped>

.el-header {
  position: fixed;
  width: 100%;
  background: #ffffff;
  color: #000000;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
  z-index: 1;
}

.el-main{
  position: relative;
  background: #f9f9f9;
  padding: 0;
  top: 70px;
  min-height: calc(100vh - 70px);
}
</style>