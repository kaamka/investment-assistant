<template>
  <v-flex xs12 sm6 offset-sm3>
    <v-expansion-panel>
      <v-expansion-panel-content
        v-for="(item,i) in 5"
        :key="i"
      >
        <div slot="header">Item</div>
        <v-card>
          <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-flex>
</template>

<script>
  export default {
    data: () => ({})
  }
</script>

<style>
v-card-title {
  font-size: 3em;
}
</style>
