#!/usr/bin/python3

from flask import Flask, jsonify, request
from reddit_sentiment_analysis import *
app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')
def get_incomes():
    print("hello")
    top, picks_ayz, scores, picks, times = main()
    print("=====================================")
    print(type(top))
    print(picks_ayz)
    return jsonify({"top":top, "scores":scores})


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204