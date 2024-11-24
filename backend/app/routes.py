from flask import Flask, jsonify, request
from scraper import scrape_data
from sentiment_analysis import analyze_sentiments
from visualization import visualize_data
from prediction import train_model

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    """Trigger data scraping."""
    scrape_data()
    return jsonify({"message": "Data scraped successfully."})

@app.route('/analyze', methods=['POST'])
def analyze():
    """Trigger sentiment analysis."""
    input_file = request.json.get('input_file', 'data/scraped_data.json')
    output_file = request.json.get('output_file', 'data/processed_data.csv')
    analyze_sentiments(input_file, output_file)
    return jsonify({"message": "Sentiment analysis completed.", "output_file": output_file})

@app.route('/visualize', methods=['GET'])
def visualize():
    """Trigger data visualization."""
    visualize_data('data/processed_data.csv')
    return jsonify({"message": "Visualization generated."})

@app.route('/train', methods=['GET'])
def train():
    """Train the predictive model."""
    train_model('data/processed_data.csv')
    return jsonify({"message": "Model training completed."})

if __name__ == "__main__":
    app.run(debug=True)
