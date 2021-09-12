<template>
  <div class="header">
    <img class="logo"
         :src="require('@/assets/logo.png')"
          @click="toHome()">
    <div class="personal">
      <el-dropdown>
        <span class="el-dropdown-link">
           <i class="el-icon-more"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>个人中心</el-dropdown-item>
          <el-dropdown-item>关于</el-dropdown-item>
          <el-dropdown-item divided>退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>

    <el-menu
        class="navbar"
        mode="horizontal"
        @select="handleSelect"
        text-color="#242738"
        active-text-color="#367bf0">
        <el-menu-item v-for="item in menuItems" :index="item.index">
          {{ item.name }}
        </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      menuItems: {
        "goods": {
          name: "物品清单",
          index: "goods",
          link: "/gds"
        },
        "summaries": {
          name: "概要",
          index: "summaries",
          link: "/sum"
        },
        "statistics": {
          name: "消费统计",
          index: "statistics",
          link: "/stat"
        },
      }
    }
  },

  methods: {
    handleSelect(index, indexPath) {
      this.$router.push(this.menuItems[index].link)
    },

    toHome() {
      this.$router.push("/home")
    }
  }

}
</script>

<style scoped>
.header {
  height: 70px;
}

.logo {
  position: relative;
  width: 150px;
  height: 60px;
  top: 5px;
  object-fit: contain;
}

.logo:hover {
  cursor: pointer;
}

.navbar {
  display: inline-block;
  float: right;
  font-size: 16px;
}

.navbar li {
  height: 70px;
  line-height: 70px;
}

.personal {
  display: inline-block;
  float: right;
  width: 80px;
  text-align: center;
}

.el-dropdown-link {
  height: 70px;
  line-height: 70px;
  font-size: 28px;

}

</style>