<template>
  <div>
    <div class="main">
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
      <div class="illustration">
        <el-image
            style="width: 500px; height: 500px"
            :src="require('@/assets/imgs/illustration.png')"
            fit="cover">
        </el-image>
      </div>
    </div>
    <div class="footer">
      <div class="title">Catculator2 ©2021 Created by TJSDD</div>
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
    width: 100%;
    height: calc(90vh - 60px);
  }

  .footer {
    position: absolute;
    width: 400px;
    height: 30px;
    bottom: 5px;
    left: calc(50% - 200px);
  }

  .title {
    color: #333;
    text-align: center;
    line-height: 30px;
    font-size: 12px;
  }

  .illustration {
    position: absolute;
    right: 100px;
    top: 50px;
  }

  .slogan {
    position: absolute;
    left: 100px;
    top: 120px;
    font-size: 56px;
    font-family: "Isla de Tabarca";
  }

  .slogan div {
    margin-bottom: 30px;
  }
</style>