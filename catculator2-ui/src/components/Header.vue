<template>
  <div class="header">
    <el-row>
      <el-col :span="1" :offset="1">
        <div class="title">Ca<span style="color: orangered">t</span>culator2</div>
      </el-col>

      <el-col :span="2" :offset="20">
       <div class="avatar">
         <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
       </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
.header {
  width: 100%;
  height: 60px;
  background-color: #ffffff;
}

.title {
  text-align: center;
  height: 60px;
  line-height: 60px;
  color: #333333;
  font-weight: bold;
  font-size: 20px;
}

.avatar {
  height: 60px;
  line-height: 60px;
}
.el-avatar {
  margin: 10px;
  margin-left: 40px;
}
</style>