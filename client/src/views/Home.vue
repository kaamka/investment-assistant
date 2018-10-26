<template>
  <v-layout row wrap>
    <funds></funds>
    <search_settings></search_settings>
    <suggestions></suggestions>
  </v-layout>
</template>

<script>
  import funds from '../components/funds'
  import suggestions from '../components/suggestions'
  import search_settings from '../components/search_settings'

  export default {
    components: {
      funds,
      suggestions,
      search_settings
    }
  }
</script>
