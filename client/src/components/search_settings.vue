<template>
  <v-flex xs12 sm6 offset-sm3 mb-3>
    <v-subheader>Ustawienia</v-subheader>
    <v-card>
      <v-layout wrap align-center>
        <v-flex xs12 sm6 d-flex>
          <v-card-title primary-title>
            <v-select
              :items="items"
              label="Czas trwania"
            ></v-select>
            <v-flex xs9>
              <v-slider
                label="Kwota"
                v-model="slider"
                :min="min"
                :max="max"
              ></v-slider>
            </v-flex>
            <v-flex xs3>
              <v-text-field
                v-model="slider"
                class="pl-3"
                type="number"
              ></v-text-field>
            </v-flex>

          </v-card-title>
        </v-flex>
      </v-layout>
    </v-card>
  </v-flex>
</template>

<script>
  export default {
    data: () => ({
      items: ['3 miesiące', '6 miesięcy', '1 rok', '2 lata'],
      slider: 5000,
      min: 0,
      max: 10000
    })
  }
</script>

<style>
v-card-title {
  font-size: 3em;
}
</style>
