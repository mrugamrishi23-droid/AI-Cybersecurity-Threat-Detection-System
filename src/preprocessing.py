from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.dropna()

    # Convert label (normal/attack) to numbers
    df['label'] = df['label'].map({'normal': 0, 'attack': 1})

    X = df.drop('label', axis=1)
    y = df['label']

    return X, y