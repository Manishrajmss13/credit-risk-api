# preprocess.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib  # for saving processed objects

# Step 1: Load the dataset
data_path = "../data/credit_data.csv"
df = pd.read_csv(data_path)


# Step 2: Separate features and target
X = df.drop("kredit", axis=1)
y = df["kredit"]

# Numeric columns
numeric_features = ["laufzeit", "hoehe", "alter"]

# Ordinal categorical columns
ordinal_features = ["laufkont", "sparkont", "beszeit", "rate", "wohnzeit", "bishkred", "pers"]

# Nominal categorical columns
nominal_features = ["moral", "verw", "famges", "buerge", "verm", 
                    "weitkred", "wohn", "beruf", "telef", "gastarb"]

# Numeric transformer: fill missing with median + scale
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Ordinal transformer: fill missing with most frequent + encode
ordinal_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder())
])

# Nominal transformer: fill missing with most frequent + one-hot encode
nominal_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine all transformers
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("ord", ordinal_transformer, ordinal_features),
        ("nom", nominal_transformer, nominal_features)
    ]
)

# Fit and transform the dataset
X_processed = preprocessor.fit_transform(X)

# Optional: convert to DataFrame (good for debugging)
X_processed_df = pd.DataFrame(X_processed.toarray() if hasattr(X_processed, "toarray") else X_processed)

# Save preprocessor for later use in API
joblib.dump(preprocessor, "../model/artifacts/preprocessor.pkl")

print("Preprocessing complete. Processed data shape:", X_processed_df.shape)

