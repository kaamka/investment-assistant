import axios from 'axios'

export const invest = axios.create({
  baseURL: `http://localhost:5000/`
})

export const banking = axios.create({
  baseURL: 'https://team7.asseco.pl/retail-banking-swagger/api/'
})
