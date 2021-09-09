<template>
  <div class="header">
    <el-row>
      <el-col :span="4">
        <div class="header-item header-item-title" @click="toHome()">
          <span class="title">Catculator2</span>
        </div>
      </el-col>
      <el-col :span="6" :offset="5">
        <div class="header-item header-item-nav">
          <el-row>
            <el-col :span="8">
              <el-tooltip class="item" effect="dark" content="物品清单" placement="bottom">
                <i class="el-icon-box" @click="toGds()"></i>
              </el-tooltip>
            </el-col>
            <el-col :span="8">
              <el-tooltip class="item" effect="dark" content="基本信息" placement="bottom">
                <i class="el-icon-tickets" @click="toStat()"></i>
              </el-tooltip>
            </el-col>
            <el-col :span="8">
              <el-tooltip class="item" effect="dark" content="数据统计" placement="bottom">
                <i class="el-icon-pie-chart" @click="toTodo()"></i>
              </el-tooltip>
            </el-col>
          </el-row>
        </div>
      </el-col>
      <el-col :span="1" :offset="8">
        <el-dropdown>
          <span class="el-dropdown-link">
            <div class="header-item header-item-more">
              <i class="el-icon-more"></i>
            </div>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>个人中心</el-dropdown-item>
            <el-dropdown-item>关于</el-dropdown-item>
            <el-dropdown-item divided>退出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    toHome() {
      this.$router.push('/home')
    },
    toGds() {
      this.$router.push('/gds')
    },
    toStat() {
      this.$router.push('/stat')
    },
    toTodo() {

    }
  }
}
</script>

<style scoped>
.header {
  width: 100%;
  height: 60px;
}

.header-item {
  width: 100%;
  height: 60px;
}

.title {
  line-height: 60px;
  font-size: 42px;
  font-weight: bolder;
  font-family: Eighty-Eight;
}

.header-item-nav, .header-item-more {
  line-height: 60px;
  text-align: center;
  font-size: 32px;
}

.el-dropdown-link {
  cursor: pointer;
}

</style>