<template>
  <div class="main">
    <div>
      <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
        <el-tab-pane label="用户管理" name="first">
          <div class="search-boxes">
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-button type="primary">Go!</el-button>
          </div>
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
        </el-tab-pane>
        <el-tab-pane label="配置管理" name="second">配置管理</el-tab-pane>
        <el-tab-pane label="角色管理" name="third">
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
        </el-tab-pane>
        <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
export default {
  name: "goods",
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
      }],
      activeName: 'first',
      input: '',
    }
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
}
</script>

<style scoped>

.main {
  width: 100%;
}

.search-boxes {

}

.el-input {
  display: inline-block;
  width: 200px;
  margin: 10px;
}

.el-button {
  margin: 10px;
}

</style>