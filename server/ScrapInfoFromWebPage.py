'''
    {
        depositName: “XXXX”,
        offered_by: "AliorBank",
        minAmount: 23323,
        maxAmount: 32343,
        forNew: true,
        interest: 3.4,
        duration: 3, //months
      sourceLink: ‘http://getin-nowa-lokata-super.com’

    }

'''


from bs4 import BeautifulSoup
import requests
import json
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

def scrap_for_get_all_available_deposits():
    depo_info_array = []
    source = requests.get('https://depozaur.pl/lokaty-bankowe/0-1000000/1d-60m?opening=internet,mobile,branch,phone').text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())

    body = soup.find('body')
    all_prods = body.find('div', id='wrapper')
    page_content = all_prods.find('div', id='page-content')



    for container in page_content.find_all('div', class_='container'):
        if container.find('div', class_='entities-result'):
            results = container.find('div', class_='', id='entities')

    for deposit in results.find_all('div', itemprop='itemListElement'):
        deposit_info = {}
        deposit_info['bank_name'] = deposit.find('span', class_="cell provider", itemprop="offeredBy").meta["content"]
        deposit_info['deposit_name'] = deposit.find('span', class_="cell product-info").h3.text
        deposit_info['min_amount'] = deposit.find('span', class_="cell product-info").ul.li.find_all('span')[0]["content"]
        try:
            deposit_info['max_amount'] = deposit.find('span',
                                                      class_="cell product-info").ul.li.find_all('span')[1]["content"]
        except Exception as e:
            deposit_info['max_amount'] = None

        if deposit.find('div', class_="product-more-info-tab").text.find("Tylko dla nowych klientów") == -1:
            deposit_info['for_new'] = False
        else:
            deposit_info['for_new'] = True
        deposit_info['interest'] = float(deposit.find('span', itemprop="interestRate").span.text)
        deposit_info['duration'] = deposit.find('span', class_="cell product-info").ul.find_all('li')[1].text
        deposit_info['link_with_offer'] = deposit.find('span', class_="cell product-check text-right").span["data-url"]
        depo_info_array.append(deposit_info)
    return depo_info_array

if __name__ == "__main__":
    deposits_json = json.dumps(scrap_for_get_all_available_deposits())
    # Write JSON file
    with io.open('data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(scrap_for_get_all_available_deposits(),
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))



