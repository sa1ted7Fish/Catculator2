<template>
  <div class="main">
    <el-tabs type="border-card">
      <el-tab-pane label="新物品">
        <router-view name="unused"></router-view>
      </el-tab-pane>
      <el-tab-pane label="使用中">
        <router-view name="inUsing"></router-view>
      </el-tab-pane>
      <el-tab-pane label="用完 or 废弃">
        <router-view name="usedUp"></router-view>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "Goods",

}
</script>

<style scoped>
.main {
  padding: 50px 100px 50px 100px;
}
</style>