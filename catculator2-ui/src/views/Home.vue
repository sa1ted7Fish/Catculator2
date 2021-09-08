<template>
  <div class="home">
    <div class="area area-1">
      <el-row>
        <el-col :span="12">
          <div style="width: 100%;height: 200px;background: deepskyblue">

          </div>
        </el-col>
        <el-col :span="12">
          <div style="width: 100%;height: 200px;background: orangered">

          </div>
        </el-col>
      </el-row>
    </div>
    <div class="area area-2">
      <el-row>
        <el-col :span="12">
          <div style="width: 100%;height: 300px;background: pink">

          </div>
        </el-col>
        <el-col :span="12">
          <div style="width: 100%;height: 300px;background: greenyellow">

          </div>
        </el-col>
      </el-row>
    </div>
    <div class="area area-3">
      <el-row>
        <el-col :span="6">
          <div style="width: 100%;height: 200px;background: bisque">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: darkgoldenrod">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: aquamarine">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: thistle">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: blueviolet">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: cornflowerblue">

          </div>
        </el-col>
        <el-col :span="3">
          <div style="width: 100%;height: 200px;background: yellow">

          </div>
        </el-col>
      </el-row>
    </div>
    <div class="footer">
      <el-row>
        <el-col :span="6" :offset="9">
          <div class="title">Catculator2 ©2021 Created by TJSDD</div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>
  .home {
    width: 100%;
  }

  .area {
    position: relative;
    width: 90%;
    left: 5%;
  }

  .area-1 {
    height: 200px;
    background: black;
  }
  .area-2 {
    height: 300px;
    background:orangered;
  }
  .area-3 {
    height: 200px;
    background: greenyellow;
  }


  .footer {
    width: 100%;
    height: 30px;
    background-color: #ffffff;
  }

  .title {
    color: #333;
    text-align: center;
    line-height: 30px;
    font-size: 12px;
  }
</style>