<template>
  <div class="main">
    <el-row>
      <el-col :span="12">
        <div class="slogan">
          <div>Calculate</div>
          <div>how much you spend</div>
          <div>on keep</div>
          <div>
            <span style="text-decoration: line-through">a cat.</span>
            &nbsp;
            <span style="color: #ef233c">a pet!</span>
          </div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="illustration">
          <img :src="require('@/assets/imgs/illustration.png')">
        </div>
      </el-col>
    </el-row>
    <div class="footer">
      <div>Catculator2 ©2021 Created by TJSDD</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>
  .main {
    position: relative;
    width: 80%;
    height: calc(100vh - 70px);
    left: 10%;
  }

  .slogan {
    position: relative;
    top: 120px;
    left: 100px;
    font-size: 56px;
    line-height: 100px;
    font-family: "Isla de Tabarca";
  }

  .illustration {
    position: relative;
    width: 500px;
    height: 500px;
    top: 80px;
  }

  .footer {
    position: absolute;
    width: 400px;
    height: 30px;
    bottom: 5px;
    left: calc(50% - 200px);
    color: #333;
    text-align: center;
    line-height: 30px;
    font-size: 12px;
  }
</style>