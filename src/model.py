from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(contamination=0.3, random_state=42)
    model.fit(X)
    return model

def predict(model, X):
    preds = model.predict(X)
    
    # Convert -1 (anomaly) → 1 (attack), 1 → 0 (normal)
    preds = [1 if x == -1 else 0 for x in preds]
    return preds