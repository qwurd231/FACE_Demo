<script setup lang="ts">
import { RouterView } from 'vue-router'
import TopBar from '@/components/header/TopBar.vue'
import TestTextArea from '@/components/body/TestTextArea.vue'
import StatisticGraph from '@/components/body/StatisticGraph.vue'
import StatisticExplanation from '@/components/body/StatisticExplanation.vue'
</script>

<template>
  <header>
    <TopBar />
  </header>

  <body>
    <div class="main_frame">
      <div class="main_part">
        <TestTextArea />
        <div class="module" style="position: absolute; top: 60%">
          <StatisticGraph />
        </div>
        <StatisticExplanation />
      </div>
    </div>
  </body>

  <RouterView />
</template>

<style scoped>
.main_frame {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.main_part {
  width: 60%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  outline: auto;
  outline-color: rgb(154, 191, 239);
}
</style>
