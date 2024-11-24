# app/scraper.py

import tweepy
import instaloader
import requests
from bs4 import BeautifulSoup
import json
import time
from app import app

# Twitter API credentials
TWITTER_API_KEY = app.config['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = app.config['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = app.config['TWITTER_ACCESS_TOKEN_SECRET']

# Set up Twitter API with Tweepy
def twitter_api_setup():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def scrape_tweets(api, query="fashion trends", count=100):
    """Scrape X tweets for sentiment analysis."""
    tweets_data = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
        tweets_data.append({
            "tweet": tweet.full_text,
            "author": tweet.user.screen_name,
            "created_at": tweet.created_at,
            "likes": tweet.favorite_count,
            "retweets": tweet.retweet_count,
            "source": "Twitter"
        })
    return tweets_data

# Instagram Scraping using instaloader
def scrape_instagram(hashtag="fashion", limit=10):
    """Scrape posts from Instagram using hashtag."""
    L = instaloader.Instaloader()

    posts_data = []
    for post in instaloader.Hashtag.from_name(L.context, hashtag).get_posts():
        if len(posts_data) >= limit:
            break
        post_info = {
            "caption": post.caption,
            "author": post.owner_username,
            "likes": post.likes,
            "comments": post.comments,
            "created_at": post.date_utc.isoformat(),
            "url": post.url,
            "source": "Instagram"
        }
        posts_data.append(post_info)
    
    return posts_data

# Scraping Fashion Product Data (ASOS, Zalando, etc.)
def scrape_asos():
    """Scrape data from ASOS."""
    BASE_URL = "https://www.asos.com/women/"
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    for product in soup.select('.product'):
        try:
            data.append({
                "name": product.select_one('.product-name').text.strip(),
                "price": product.select_one('.product-price').text.strip(),
                "image_url": product.select_one('img')['src'],
                "category": product.select_one('.product-category').text.strip(),
                "description": product.select_one('.product-description').text.strip(),
                "source": "ASOS"
            })
        except AttributeError:
            continue
    return data

# Combine all data sources
def scrape_all():
    """Scrape data from all sources."""
    api = twitter_api_setup()

    print("Scraping ASOS...")
    asos_data = scrape_asos()
    print(f"Scraped {len(asos_data)} items from ASOS.")

    print("Scraping Twitter...")
    twitter_data = scrape_tweets(api, query="fashion trends", count=100)
    print(f"Scraped {len(twitter_data)} tweets from Twitter.")

    print("Scraping Instagram...")
    instagram_data = scrape_instagram(hashtag="fashion", limit=10)
    print(f"Scraped {len(instagram_data)} posts from Instagram.")

    all_data = asos_data + twitter_data + instagram_data

    with open("data/scraped_data.json", "w") as f:
        json.dump(all_data, f, indent=4)
    print("All data scraped and saved to data/scraped_data.json")
