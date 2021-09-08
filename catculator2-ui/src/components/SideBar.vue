<template>
  <div class="menu">
    <div class="logo">
      <el-image
          style="width: 50px; height: 50px"
          src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
          fit="cover">
      </el-image>
    </div>

    <el-tooltip class="item" effect="dark" content="首页" placement="right">
      <div class="menu-item menu-item-1" @click="toHome()">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'home']" /></div>
      </div>
    </el-tooltip>

    <el-tooltip class="item" effect="dark" content="物品列表" placement="right">
      <div class="menu-item menu-item-2">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'money-check']" /></div>
      </div>
    </el-tooltip>

    <el-tooltip class="item" effect="dark" content="消费统计" placement="right">
      <div class="menu-item menu-item-3">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'chart-line']" /></div>
      </div>
    </el-tooltip>

    <el-tooltip class="item" effect="dark" content="设置" placement="right">
      <div class="menu-item menu-item-4">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'cog']" /></div>
      </div>
    </el-tooltip>

    <el-tooltip class="item" effect="dark" content="关于" placement="right">
      <div class="menu-item menu-item-5">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'info']" /></div>
      </div>
    </el-tooltip>

    <el-tooltip class="item" effect="dark" content="退出" placement="right">
      <div class="menu-item menu-item-exit">
        <div class="menu-item-icon"><font-awesome-icon :icon="['fas', 'sign-out-alt']" /></div>
      </div>
    </el-tooltip>

  </div>
</template>

<script>
export default {
  name: "SideBar",
  methods: {
    toHome() {
      this.$router.push({path: "/home"})
    }
  }
}
</script>

<style scoped>

.logo {
  position: relative;
  width: 50px;
  height: 50px;
  margin: 5px;
}

.menu-item {
  width: 60px;
  height: 60px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.menu-item-1 {
  margin-top: calc(50vh - 260px);
}

.menu-item-exit {
  position: absolute;
  bottom: 10px;
}

.menu-item-icon {
  line-height: 40px;
  font-size: 20px;
  color: #ADB5BD;
}

.menu-item-icon:hover {
  color: #333333;
  border-left: 5px solid #48CAE4;
  background: #CAF0F8;
}

</style>