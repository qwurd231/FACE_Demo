<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Statistic Graph</h1>
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Statistic Graph</h5>
                <p class="card-text">This is a graph of the statistics of the user.</p>
                <router-link to="/history" class="btn btn-primary">History</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Statistic Graph</h5>
                <p class="card-text">This is a graph of the statistics of the user.</p>
                <router-link to="/settings" class="btn btn-primary">Settings</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
declare module '@/components/body/StatisticGraph.vue' {}
</script>
