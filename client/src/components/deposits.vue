<template>
  <v-flex xs12 sm6 offset-sm3>
    <v-subheader>Twoje lokaty</v-subheader>
    <v-expansion-panel
      v-model="panel"
      expand>
      <v-expansion-panel-content
        v-for="(item,i) in options"
        :key="i"
      >
        <div slot="header">
          <v-layout>
          <v-flex xs3 sm2 md1>
            <v-avatar
              slot="activator"
              size="36px"
              v-if="item.interest > 2"
            >
              <v-icon color="success">done_all</v-icon>
            </v-avatar>
            <v-avatar
              slot="activator"
              size="36px"
              v-else
            >
              <v-icon
                color="error">error</v-icon>
            </v-avatar>
          </v-flex>
          <v-flex xs3 sm2 md1><span class="deposit-pct">{{item.interest}}%</span></v-flex>
          <v-flex xs6 sm10 md11><span class="deposit-text">{{item.name}}</span></v-flex>

          </v-layout>
        </div>
        <v-card>
          <v-card-text v-if="item.interest > 2">Opis lokaty.</v-card-text>
          <v-card-text v-else>
            Możesz zarabiać więcej! Rozważ zakończenie lokaty i otwarcie jednej z sugerowanych.
          </v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-flex>
</template>

<script>
  export default {
    data: () => ({
      panel: [false, true, false],
      options: [
        { 
          name: 'Lokata Korzystna',
          interest: 2.7
        },
        {
          name: 'Lokata mobilna',
          interest: 1.5
        },
        {
          name: 'Lokata urodzinowa',
          interest: 2.5
        }
      ]
    })
  }
</script>

<style>
v-card-title {
  font-size: 3em;
}

.deposit-pct {
  font-size: 20px;
  line-height: 36px;
}

.deposit-text {
  line-height: 36px;
}
</style>
