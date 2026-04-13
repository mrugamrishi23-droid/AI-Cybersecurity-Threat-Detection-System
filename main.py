from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model, predict
from src.evaluate import evaluate_model
from src.visualize import plot_results

def main():
    df = load_data("data/dataset.csv")
    X, y = preprocess_data(df)

    model = train_model(X)
    predictions = predict(model, X)

    evaluate_model(y, predictions)
    plot_results(y, predictions)

if __name__ == "__main__":
    main()