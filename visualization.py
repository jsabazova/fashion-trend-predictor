import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def visualize_data(input_file):
    """Visualizes sentiment trends."""
    df = pd.read_csv(input_file)

    # Sentiment Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sentiment'], kde=True, color="skyblue", bins=20)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

    # Word Cloud
    text = ' '.join(df['cleaned_description'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Fashion Descriptions')
    plt.show()

if __name__ == "__main__":
    visualize_data("data/processed_data.csv")
