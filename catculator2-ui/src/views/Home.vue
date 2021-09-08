<template>
  <div class="home">
    <div class="area area-1">
      <el-row>
        <el-col :span="12">
          <div style="width: 100%;height: 200px;">
            <div style="height: 80px">
              <span style="position: relative;left: 40px;font-size: 28px;font-weight: bolder;line-height: 80px;color: #343a40">
                欢迎回来，Username
              </span>
            </div>
            <el-row>
              <el-col :span="6" :offset="1">
                <el-card shadow="never" class="card card-1">
                  <div style="font-size: 16px;font-weight: bold">
                    <font-awesome-icon :icon="['fas', 'yen-sign']" style="color: limegreen"/>&nbsp;&nbsp;&nbsp;总计
                  </div>
                  <div class="my-divider"></div>
                  <div style="font-size: 20px;font-weight: bold">
                    ￥12340.70
                  </div>
                </el-card>
              </el-col>
              <el-col :span="6" :offset="2">
                <el-card shadow="never" class="card card-2">
                  <div style="font-size: 16px;font-weight: bold">
                    <font-awesome-icon :icon="['fas', 'calendar-check']" style="color: orange"/>&nbsp;&nbsp;&nbsp;当月
                  </div>
                  <div class="my-divider"></div>
                  <div style="font-size: 20px;font-weight: bold">
                    ￥158.20
                  </div>
                </el-card>
              </el-col>
              <el-col :span="6" :offset="2">
                <el-card shadow="never" class="card card-3">
                  <div style="font-size: 16px;font-weight: bold">
                    <font-awesome-icon :icon="['fas', 'percent']" style="color: red"/>&nbsp;&nbsp;&nbsp;月收入占比
                  </div>
                  <div class="my-divider"></div>
                  <div style="font-size: 20px;font-weight: bold">
                    12.86%
                  </div>
                </el-card>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="12">
          <div style="width: 100%;height: 200px;background: linear-gradient(to right, #6190e8, #a7bfe8);border-radius: 24px">
            <div style="position:relative;left: 80px;top: 20px;height: 50px;line-height: 50px;font-size: 36px;color: #ffffff;font-family: xkcd">
              Calculate<br/>how much you spend<br/>on keep <span style="text-decoration: line-through">a cat.</span><span style="color: #ff0a37">&nbsp;&nbsp;a pet!</span>
            </div>
            <el-image
                style="position: absolute;width: 160px; height: 160px;right: 80px; top: 20px"
                :src="require('@/assets/imgs/claw.png')"
                fit="cover">
            </el-image>
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
          <div style="width: 100%;height: 300px;background: bisque">

          </div>
        </el-col>
        <el-col :span="6">
          <div style="width: 100%;height: 300px;background: darkgoldenrod">

          </div>
        </el-col>
        <el-col :span="6">
          <div style="width: 100%;height: 300px;background: aquamarine">

          </div>
        </el-col>
        <el-col :span="6">
          <div style="width: 100%;height: 300px;background: thistle">

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
  }
  .area-2 {
    height: 300px;
  }
  .area-3 {
    height: 300px;
  }

  .card {
    width: 100%;
    height: 120px;
    border: none;
    text-align: center;
    color: #343a40;
  }

  .my-divider {
    width: 90%;
    height: 1px;
    background: lightgray;
    margin-left: 5%;
    margin-right: 5%;
    margin-top: 10px;
    margin-bottom: 10px;
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