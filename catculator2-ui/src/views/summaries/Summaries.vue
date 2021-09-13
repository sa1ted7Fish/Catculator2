<template>
  <div class="main">
    <el-row :gutter="50">
      <el-col :span="18">
        <el-row :gutter="50">
          <el-col :span="8">
            <el-card class="basic-info basic-info-1">
              <div class="data">
                <el-image
                    style="position: absolute;width: 100px;height: 100px;top: 30px;left: 30px"
                    :src="require('@/assets/imgs/money.png')"
                    fit="cover">
                </el-image>
                <div class="text">
                  <span style="font-size: 20px;font-weight: bold;">当年消费</span>
                  <span style="font-size: 18px;color: #636363;line-height: 60px">￥4523.60</span>
                </div>
              </div>
              <div class="description">
                <span>
                  这一年到目前为止的宠物消费总额。
                </span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card class="basic-info basic-info-2">
              <div class="data">
                <el-image
                    style="position: relative;width: 100px;height: 100px;top: 30px;left: 30px"
                    :src="require('@/assets/imgs/calendar.png')"
                    fit="cover">
                </el-image>
                <div class="text">
                  <span style="font-size: 20px;font-weight: bold;">当月消费</span>
                  <span style="font-size: 18px;color: #636363;line-height: 60px">￥237.30</span>
                </div>
              </div>
              <div class="description">
                这一月到目前为止的宠物消费总额。
              </div>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card class="basic-info basic-info-3">
              <div class="data">
                <el-image
                    style="position: relative;width: 100px;height: 100px;top: 30px;left: 30px"
                    :src="require('@/assets/imgs/statistic.png')"
                    fit="cover">
                </el-image>
                <div class="text">
                  <span style="font-size: 20px;font-weight: bold;">消费/收入</span>
                  <span style="font-size: 18px;color: #636363;line-height: 60px">18.37%</span>
                </div>
              </div>
              <div class="description">
                这一月到目前为止宠物消费占月收入的比例。
              </div>
            </el-card>
          </el-col>
        </el-row>

        <el-row :gutter="50" style="margin-top: 50px">
          <el-col :span="12">
            <el-card class="remain" style="width: 100%;height: 360px">
              <div class="title">
                常用消耗品剩余
              </div>
              <div class="table">
                <el-table
                    :data="tableData"
                    style="width: 100%;"
                    :show-header="false"
                    max-height="250px">
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
                </el-table>
              </div>
            </el-card>
          </el-col>
          <el-col :span="12">
            <el-card class="days" style="width: 100%;height: 360px">
              <div class="title">
                距离上一次天数
              </div>
              <div class="table">
                <el-table
                    :data="tableData"
                    style="width: 100%;"
                    :show-header="false"
                    max-height="250px">
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
                </el-table>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="6">
        <el-card class="todo-list" style="width: 100%;height: 650px">
          <div class="title">
            待办事项
          </div>
          <div class="items">
            <el-card class="item">1</el-card>
            <el-card class="item">2</el-card>
            <el-card class="item">3</el-card>
            <el-card class="item">4</el-card>
            <el-card class="item">5</el-card>
            <el-card class="item">6</el-card>
            <el-card class="item">7</el-card>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Summaries",
  data() {
    return {
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
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      },]
    }
  }
}
</script>

<style scoped>
.main {
  padding: 50px 100px 50px 100px;
}

.basic-info {
  width: 100%;
  height: 240px;
}

.basic-info /deep/ .el-card__body,
.remain /deep/ .el-card__body,
.days /deep/ .el-card__body,
.todo-list /deep/ .el-card__body {
  padding: 0;
}

.basic-info .data {
  position: relative;
}

.basic-info .data div {
  display: inline-block;
}

.basic-info-1 .data {
  width: 100%;
  height: 160px;
  background-image: linear-gradient(120deg, #c5fff4 -10%, white 110%);
}

.basic-info-2 .data {
  width: 100%;
  height: 160px;
  background-image: linear-gradient(120deg, #d9eef2 -10%, white 110%);
}

.basic-info-3 .data {
  width: 100%;
  height: 160px;
  background-image: linear-gradient(120deg, #cddbee -10%, white 110%);
}

.basic-info .data .text {
  position: absolute;
  width: calc(100% - 190px);
  height: 100px;
  top: 30px;
  right: 30px;
}

.basic-info .description {
  padding: 20px;
  font-size: 16px;
  color: #636363;
}

.remain .title,
.days .title,
.todo-list .title {
  width: 100%;
  height: 40px;
  padding: 20px 30px 20px 30px;
  font-size: 20px;
  line-height: 40px;
  font-weight: bold;
  color: #333333;
}

.remain {
  background-image: linear-gradient(120deg, #f2d9e3 -10%, white 110%);
}

.days {
  background-image: linear-gradient(120deg, #f2e8d9 -10%, white 110%);
}

.todo-list {
  background-image: linear-gradient(120deg, #dfdfdf -10%, white 110%);
}

.table {
  margin: 0 30px 0 30px;
}

/*.el-table::-webkit-scrollbar{*/
/*  display: none;*/
/*}*/

.todo-list .items {
  padding: 30px;
  padding-top: 0;
  height: 570px;
  overflow: auto;
}

.todo-list .items .item {
  height: 160px;
  margin-bottom: 30px;
  border-radius: 8px;
}

/*.todo-list .items::-webkit-scrollbar {*/
/*  display: none;*/
/*}*/

</style>