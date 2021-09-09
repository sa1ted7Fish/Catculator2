<template>
  <div class="main">
    <div class="container container-1">
      <el-row>
        <el-col :span="16">
          <div style="height: 500px">

          </div>
        </el-col>
        <el-col :span="8">
          <div class="calendar">
            <el-calendar v-model="value"></el-calendar>
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
      value: new Date()
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
  background: #fffdf7;
  margin-bottom: 10px;
}

.container-1 {
  height: 800px;
}

.calendar {
  width: 100%;
}

.calendar /deep/ .el-calendar-table .el-calendar-day {
  height: 50px;
}

</style>