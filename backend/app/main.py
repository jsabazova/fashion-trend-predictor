import os
from scraper import scrape_data
from sentiment_analysis import analyze_sentiments
from visualization import visualize_data
from prediction import train_model

def main():
    """Runs the complete fashion trend prediction pipeline."""
    print("Step 1: Scraping Data...")
    scrape_data()

    print("\nStep 2: Analyzing Sentiments...")
    analyze_sentiments("data/scraped_data.json", "data/processed_data.csv")

    print("\nStep 3: Visualizing Data...")
    visualize_data("data/processed_data.csv")

    print("\nStep 4: Training Prediction Model...")
    train_model("data/processed_data.csv")

if __name__ == "__main__":
    main()
