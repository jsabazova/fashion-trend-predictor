# app/sentiment_analysis.py

from textblob import TextBlob

def analyze_sentiment(data):
    sentiments = []
    for item in data:
        if "tweet" in item:
            text = item["tweet"]
        elif "caption" in item:
            text = item["caption"]
        else:
            continue
        
        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity  # Sentiment polarity score
        sentiments.append({
            "text": text,
            "sentiment": sentiment
        })
    
    return sentiments
