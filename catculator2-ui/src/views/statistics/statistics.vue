<template>
  <div class="main">
    <div class="container container-1">
      <el-row>
        <el-col :span="18">
          <div class="area area-left" style="width: calc(100% - 40px)">
            <div class="general-infos">
              <el-row>
                <el-col :span="8">
                  <div class="general-info general-info-total">
                    <el-image
                        style="width: 100px;height: 100px"
                        :src="require('@/assets/imgs/money.png')"
                        fill="cover">
                    </el-image>
                    <div class="general-info-title">
                      总计支出
                    </div>
                    <div class="general-info-data">
                      <span style="color: red">￥</span>23453.40
                    </div>
                    <div class="general-info-divider"></div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="general-info general-info-monthly">
                    <el-image
                        style="width: 100px;height: 100px"
                        :src="require('@/assets/imgs/calendar.png')"
                        fill="cover">
                    </el-image>
                    <div class="general-info-title">
                      当月支出
                    </div>
                    <div class="general-info-data">
                      <span style="color: green">￥</span>145.70
                    </div>
                    <div class="general-info-divider"></div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="general-info general-info-ratio">
                    <el-image
                        style="width: 100px;height: 100px"
                        :src="require('@/assets/imgs/statistic.png')"
                        fill="cover">
                    </el-image>
                    <div class="general-info-title">
                      月支出/月薪
                    </div>
                    <div class="general-info-data">
                      24.58<span style="color: blue">%</span>
                    </div>
                    <div class="general-info-divider"></div>
                  </div>
                </el-col>
              </el-row>
            </div>
            <div class="current-using">
              <div class="current-using-title">
                正在使用
              </div>
              <div class="current-using-list">
                <el-table
                    :data="tableData"
                    style="position: relative;width: 90%;left: 5%;height: 250px;overflow: auto;top: 70px"
                    :show-header="false"
                    stripe>
                  <el-table-column
                      prop="date"
                      label="日期"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="name"
                      label="姓名"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="address"
                      label="地址">
                  </el-table-column>
                </el-table>
              </div>
            </div>
            <el-row>
              <el-col :span="12">
                <div class="other-info other-info-inventory">
                  <div class="other-info-title">
                    常用消耗品余量
                  </div>
                </div>
              </el-col>
              <el-col :span="12">
                <div class="other-info other-info-days">
                  <div class="other-info-title">
                    距离上一次天数
                  </div>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="area area-right">
            <div class="carousel">
              <el-carousel trigger="click" height="380px" style="border-radius: 8px" :interval="4000">
                <el-carousel-item v-for="item in imgList" :key="item">
                  <img
                    style="width: 100%;height: 100%"
                    :src="item"
                    fit="cover">
                  </img>
                </el-carousel-item>
              </el-carousel>
            </div>
            <div class="todo-list">
              <div class="todo-list-title">
                待办事项
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "statistics",
  data() {
    return {
      imgList: [
        require('@/assets/imgs/with-cat-1.png'),
        require('@/assets/imgs/with-dog-1.png'),
        require('@/assets/imgs/with-cat-2.png'),
        require('@/assets/imgs/with-dog-2.png')
      ],
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      },]
    }
  }
}
</script>

<style scoped>
.main {
  width: 100%;
}

.container {
  width: 100%;
  /*background: #fffdf7;*/
  margin-top: 60px;
  margin-bottom: 10px;
}

.container-1 {
  height: 800px;
}

.general-infos, .general-info {
  position: relative;
  height: 140px;
}

.general-info {
  border-radius: 8px;
  background: white;
}

.general-info-total {
  margin-right: 24px;
}

.general-info-monthly {
  margin-left: 12px;
  margin-right: 12px;
}

.general-info-ratio {
  margin-left: 24px;
}

.el-image {
  position: absolute;
  left: 20px;
  top: -30px;
}

.general-info-title, .general-info-data {
  position: absolute;
  right: 20px;
}

.general-info-title {
  top: 20px;
  font-size: 16px;
  color: gray;
}

.general-info-data {
  top: 60px;
  font-size: 20px;
  font-weight: bold;
  color: #333333;
}

.general-info-divider {
  position: absolute;
  bottom: 45px;
  height: 1px;
  background: gray;
  width: 90%;
  left: 5%;
}

.current-using {
  position: relative;
  width: 100%;
  height: 360px;
  background: white;
  margin-top: 40px;
  border-radius: 8px;
  overflow: auto;
}

.current-using-title {
  position: absolute;
  height: 50px;
  line-height: 50px;
  left: 5%;
  font-size: 20px;
  color: gray;
  margin-top: 20px;
}

.other-info {
  position: relative;
  width: calc(100% - 20px);
  height: 320px;
  margin-top: 40px;
  background: white;
  border-radius: 8px;
}

.other-info-inventory {
  margin-right: 20px
}

.other-info-title {
  position: absolute;
  height: 50px;
  line-height: 50px;
  left: 10%;
  font-size: 20px;
  color: gray;
  margin-top: 20px;
}

.other-info-days {
  margin-left: 20px
}

.carousel {
  position: relative;
  width: 100%;
  height: 360px;
  background: white;
  border-radius: 8px;
}

.todo-list {
  position: relative;
  width: 100%;
  height: 500px;
  margin-top: 40px;
  background: white;
  border-radius: 8px;
}

.todo-list-title {
  position: absolute;
  height: 50px;
  line-height: 50px;
  left: 10%;
  font-size: 20px;
  color: gray;
  margin-top: 20px;
}

</style>