<template>
  <v-flex xs12 sm6 offset-sm3>
    <v-subheader>Sugerowane lokaty</v-subheader>
    <v-expansion-panel>
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
            >
              <v-icon>account_balance_wallet</v-icon>
            </v-avatar>
          </v-flex>
          <v-flex xs3 sm2 md1><span class="deposit-pct">{{item.interest}}</span></v-flex>
          <v-flex xs6 sm10 md11><span class="deposit-text">{{item.name}}</span></v-flex>

          </v-layout>
        </div>
        <v-card>
          <v-card-text>Opis lokaty.</v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-flex>
</template>

<script>
  export default {
    data: () => ({
      options: [
        {
          name: 'Lokata Witaj',
          interest: '4%'
        },
        {
          name: 'Lokata na start',
          interest: '4%',
        },
        { 
          name: 'Lokata Happy',
          interest: '3%'
        },
        {
          name: 'Lokata mobilna',
          interest: '3%'
        },
        {
          name: 'Lokata urodzinowa',
          interest: '2.5%'
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
