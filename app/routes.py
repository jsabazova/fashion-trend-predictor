# app/routes.py

from flask import render_template, request, jsonify
from app import app
from app.scraper import scrape_all
from app.sentiment_analysis import analyze_sentiment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # Call the scraper to fetch data
    scrape_all()
    return jsonify({"message": "Scraping complete!"})

@app.route('/sentiment', methods=['GET'])
def sentiment():
    # Example of fetching sentiment predictions for scraped data
    data_file = 'data/scraped_data.json'
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    sentiments = analyze_sentiment(data)
    return jsonify({"sentiments": sentiments})
