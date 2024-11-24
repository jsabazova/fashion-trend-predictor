import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(input_file):
    """Trains a sentiment-based trend prediction model."""
    df = pd.read_csv(input_file)
    df['label'] = pd.qcut(df['sentiment'], q=3, labels=["low", "medium", "high"])  # Example labeling

    # Features and Labels
    X = df[['sentiment']]
    y = df['label']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

if __name__ == "__main__":
    train_model("data/processed_data.csv")
