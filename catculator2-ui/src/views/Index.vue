<template>
  <el-container style="min-height: 100vh">
    <el-header><Header></Header></el-header>
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
.el-container {
  background-color: #FFE5A8;
}
.el-header {
  margin: 5vh 5vw 0 5vw;
  padding: 0;
}

.el-main {
  margin: 0 5vw 5vh 5vw;
  padding: 0;
}

</style>