import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/<funds>/<duration>")
def get_lokaty(funds, duration):
    lokaty_by_funds = select_by_funds({'funds': funds}, get_all_available_deposits())
    #print(lokaty_by_funds)
    lokaty_by_funds_and_duration = select_by_duration({'max_duration': int(duration)}, lokaty_by_funds)
    #print(lokaty_by_funds_and_duration)
    return jsonify(lokaty_by_funds_and_duration)


def get_all_available_deposits():
    with open('data.json') as data_file:
        all_available_deposits = json.load(data_file)
    return all_available_deposits


def select_by_funds(users_preferences, all_available_deposits):
    available_funds = users_preferences.get('funds')
    deposits_available_by_funds = []
    for item in all_available_deposits:
        if float(available_funds) >= float(item["min_amount"]):
            deposits_available_by_funds.append(item)
    return deposits_available_by_funds


def select_by_duration(users_preferences, all_available_deposits):
    max_duration = users_preferences.get('max_duration')
    deposits_available_by_duration = []
    for item in all_available_deposits:
        if max_duration >= item["duration"]:
            deposits_available_by_duration.append(item)
    return deposits_available_by_duration



if __name__ == "__main__":
    search = request.args.get("search")
    page = request.args.get("page")

    users_preferences = {'funds': 500.0, 'max_duration': 5}
    deposits_available_by_funds = select_by_funds(users_preferences, get_all_available_deposits())
    deposits_available_by_funds_and_duration = select_by_duration(users_preferences, deposits_available_by_funds)
    print(deposits_available_by_funds_and_duration)
