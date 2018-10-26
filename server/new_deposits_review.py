'''
    {
        depositName: “XXXX”,
        minAmount: 23323,
        maxAmount: 32343,
        forNew: true,
        interest: 3.4,
        duration: 3, //months
      sourceLink: ‘http://getin-nowa-lokata-super.com’
      offered_by: "AliorBank"
    }

'''


from bs4 import BeautifulSoup
import requests

depo_info_array = []
source = requests.get('https://depozaur.pl/lokaty-bankowe/0-1000000/1d-60m?opening=internet,mobile,branch,phone').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

#print(soup.find('div', class_='product deposit'))

body = soup.find('body')
#print(body)
all_prods = body.find('div', id='wrapper')
page_content = all_prods.find('div', id='page-content')
#results = ""
for container in page_content.find_all('div', class_='container'):
    if container.find('div', class_='entities-result'):
        results = container.find('div', class_='', id='entities')
        #deposits = results.find('div', itemprop="itemListElement")
        #print(deposits)


for deposit in results.find_all('div', itemprop='itemListElement'):
    deposit_info = {}
    deposit_info['bank_name'] = deposit.find('span', class_="cell provider", itemprop="offeredBy").meta["content"]
    deposit_info['deposit_name'] = deposit.find('span', class_="cell product-info").h3.text
    print(deposit_info)




