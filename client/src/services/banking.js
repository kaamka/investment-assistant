import { banking } from '@/services/api'
import { customers } from '@/services/customers'

const customer = customers[0]

export default {
  async userInfo() {
    console.debug('Getting user info')
    console.debug(customer)
    // console.debug(await banking.get(''))
    const url = `user/get/user_personal_details.json?customerId=${customer.customerId}`
    console.debug(url)
    let customerInfo = await banking.get(
      url,
      {
        headers: {
          // 'Authorization': customer.jwtToken
        }
      }
    )
    console.debug(customerInfo)

  }
}