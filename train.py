import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from feature_extraction import extract_url_features

DATA_PATH = 'datasets/legit-phish.csv'
MODEL_PATH = 'best_model.joblib'


def train():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=['ClassLabel'])
    df = df.drop_duplicates(subset=["URL"], keep='first').reset_index(drop=True)

    features = pd.DataFrame(
        df['URL'].apply(extract_url_features).to_list(),
        index=df.index
    )

    features['target'] = df['ClassLabel'].astype(int)

    df_train, df_test = train_test_split(features, test_size=0.2, random_state=42, stratify=features['target'])

    X_train = df_train.drop(columns=['target'])
    X_test = df_test.drop(columns=['target'])

    y_train = df_train['target']
    y_test = df_test['target']

    model = RandomForestClassifier(
        max_depth=20,
        max_features="log2",
        min_samples_leaf=1,
        min_samples_split=3,
        n_estimators=443,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    print(f"the model is successfully saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train()