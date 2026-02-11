# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib

# Load dataset
data_path = "../data/credit_data.csv"
df = pd.read_csv(data_path)

X = df.drop("kredit", axis=1)
y = df["kredit"]

# Load preprocessor
preprocessor = joblib.load("artifacts/preprocessor.pkl")

# Preprocess features
X_processed = preprocessor.transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=42, stratify=y
)

# Initialize models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42)
}

# Train & evaluate
for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

# Choose best model (here Random Forest) and save
best_model = models["RandomForest"]
joblib.dump(best_model, "model.pkl")
print("Model training complete. Random Forest saved as model.pkl")
