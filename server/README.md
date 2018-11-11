# Investment Assistant Backend

## Prerequisites
To run the application you need the following packages:
* Flask
* flask_cors
* bs4 

## Get deposit data
You need to acquire the data and store it in a json file. (<- do not do it if you don't need new data, since we already have it)

To scrape the webpage and save results into .json file:
```sh
python ScrapInfoFromWeb.py
```

## Run flask application
To run the app, type:
```sh
FLASK_APP=SelectGoodDeposits.py flask run
```

It is available at a url:
`http://127.0.0.1:5000/<funds>/<max_duration>`
