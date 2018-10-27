# Backend
0. INSTALLATION REQS
a. Flask
b. flask_cors
c. bs4 

1. CREATE NEW JSON FILE (<- do not do it since we already have it)
a. scraping the webpage and save results into .json file:
$ python ScrapInfoFromWeb.py


2. RUN FLASK APP
a. run app
$ FLASK_APP=SelectGoodDeposits.py flask run
b. open app in browser:
http://127.0.0.1:5000/<funds>/<max_duration>