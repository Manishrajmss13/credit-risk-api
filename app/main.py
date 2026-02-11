# app/main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
import logging
from app.schemas import Applicant

app = FastAPI(
    title="Credit Risk Scoring API",
    description="Predict probability of default and assign risk tier",
    version="1.0"
)

# Load preprocessor and model
preprocessor = joblib.load("C:\\Users\\ELCOT\\Desktop\\Projects\\credit-risk-api\\model\\artifacts\\preprocessor.pkl")
model = joblib.load("C:\\Users\\ELCOT\\Desktop\\Projects\\credit-risk-api\\model\\model.pkl")

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Risk tier logic
def risk_tier(prob):
    if prob < 0.3:
        return "LOW"
    elif prob < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"

# API root
@app.get("/")
def root():
    return {"message": "Credit Risk Scoring API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(applicant: Applicant):
    try:
        data = pd.DataFrame([applicant.model_dump()])
        X_processed = preprocessor.transform(data)
        prob = model.predict_proba(X_processed)[:, 1][0]
        tier = risk_tier(prob)
        return {"probability": round(prob, 4), "risk_tier": tier}
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})

# Helper to get feature names from preprocessor
def get_feature_names(preprocessor):
    """Get the feature names after preprocessing"""
    try:
        # Works for ColumnTransformer with transformers
        feature_names = preprocessor.get_feature_names_out()
        return feature_names
    except Exception as e:
        logger.warning(f"Could not get feature names from preprocessor: {e}")
        # fallback: return generic names
        n_features = model.n_features_in_ if hasattr(model, "n_features_in_") else 0
        return [f"feature_{i}" for i in range(n_features)]

# Feature importance endpoint
@app.get("/feature-importance")
def feature_importance():
    try:
        # Extract actual feature names after preprocessing
        feature_names = get_feature_names(preprocessor)
        importances = model.feature_importances_

        if len(feature_names) != len(importances):
            return JSONResponse(
                status_code=500,
                content={
                    "error": f"Feature count mismatch: {len(feature_names)} names vs {len(importances)} importances"
                }
            )

        # Make DataFrame for sorting and plotting
        fi_df = pd.DataFrame({"feature": feature_names, "importance": importances})
        fi_df.sort_values(by="importance", ascending=False, inplace=True)

        # Save chart as PNG
        os.makedirs("model/artifacts", exist_ok=True)
        plt.figure(figsize=(10,6))
        plt.barh(fi_df["feature"], fi_df["importance"])
        plt.xlabel("Importance")
        plt.title("Feature Importance")
        plt.gca().invert_yaxis()  # Highest importance on top
        plt.tight_layout()
        plt.savefig("model/artifacts/feature_importance.png")
        plt.close()

        # Return JSON for frontend
        return fi_df.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Feature importance failed: {e}")
        return JSONResponse(status_code=400, content={"error": str(e)})
