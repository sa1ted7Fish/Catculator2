<template>
  <div class="used-up">
    <div class="title">
      用完 or 废弃
    </div>
    <el-card class="card-search" shadow="never">
      <el-input class="search" placeholder="请输入内容"></el-input>
      <el-input class="search" placeholder="请输入内容"></el-input>
      <el-input class="search" placeholder="请输入内容"></el-input>
      <el-input class="search" placeholder="请输入内容"></el-input>
    </el-card>
    <el-card class="card-table" shadow="never">
      <el-table
          :data="tableData"
          style="width: 100%">
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
    </el-card>
  </div>
</template>

<script>
export default {
  name: "UsedUp",
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
      },]
    }
  }
}
</script>

<style scoped>
.title {
  margin: 10px 20px 20px 20px;
}

.search {
  width: 300px;
  display: inline-block;
}
</style>