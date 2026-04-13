import matplotlib.pyplot as plt

def plot_results(y, preds):
    plt.figure()
    plt.scatter(range(len(preds)), preds)
    plt.title("Anomaly Detection Results")
    plt.xlabel("Index")
    plt.ylabel("Prediction (1=Attack, 0=Normal)")
    plt.show()