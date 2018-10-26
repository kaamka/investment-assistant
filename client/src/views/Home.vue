<template>
  <v-layout row wrap>
    <funds></funds>
    <suggestions></suggestions>
  </v-layout>
</template>

<script>
  import funds from '../components/funds'
  import suggestions from '../components/suggestions'

  export default {
    components: {
      funds,
      suggestions
    }
  }
</script>
