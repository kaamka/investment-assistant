<template>
  <v-layout row wrap>
    <deposits></deposits>
    <suggestions></suggestions>
  </v-layout>
</template>

<script>
import deposits from '../components/deposits'
import suggestions from '../components/suggestions'

export default {
  components: {
    deposits,
    suggestions
  }
}
</script>
