# Credit Risk Prediction API

A FastAPI-based project for predicting credit risk using a structured dataset of client financial and personal information. This project demonstrates end-to-end data processing, **Random Forest** model integration, and a REST API deployment.

---

## 📋 Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Testing with Postman](#testing-with-postman)
- [Testing with Swagger UI](#testing-with-swagger-ui)
- [Feature Importance](#feature-importance)
- [Screenshots](#screenshots)
- [Notes](#notes)

---

## Dataset

- **Source:** Public credit dataset (German credit-like dataset)  
- **Description:** Contains 1000+ entries of clients with features describing financial status, personal information, and loan details.  
- **Target Variable:** Credit risk classification (`good` / `bad`).  
- **Size:** ~1000 records with 20 input features

---

## Features

The dataset includes features such as:

| Feature | Description |
|---------|-------------|
| `laufkont` | Checking account status |
| `laufzeit` | Loan duration (months) |
| `moral` | Credit history / moral rating |
| `verw` | Existing commitments |
| `hoehe` | Loan amount |
| `sparkont` | Savings account status |
| `beszeit` | Duration at current job |
| `rate` | Installment rate |
| `famges` | Family status / dependents |
| `buerge` | Guarantor information |
| `wohnzeit` | Residence duration |
| `verm` | Property ownership status |
| `alter` | Age |
| `weitkred` | Other existing loans |
| `wohn` | Housing type |
| `bishkred` | Existing credits |
| `beruf` | Job type |
| `pers` | Personal status / sex |
| `telef` | Telephone availability |
| `gastarb` | Foreign worker status |

> The full feature list is implemented in the Pydantic schema for validation.

---

## Model Details

### Algorithm: Random Forest Classifier

The project implements a **Random Forest** ensemble learning model that:

- Combines multiple decision trees for robust predictions
- Handles non-linear relationships in credit risk data
- Provides feature importance rankings
- Offers good generalization to unseen data


---

## Project Structure

```
credit-risk-api/
├─ app/
│  ├─ main.py           # FastAPI application & endpoints
│  ├─ schemas.py        # Pydantic request validation models
│  └─ __init__.py       # Package initialization
├─ data/
│  └─ credit_data.csv   # Raw dataset
├─ model/
│  ├─ preprocess.py     # Data cleaning & transformation
│  ├─ train.py          # Model training & evaluation
│  └─ artifacts/        # Trained models & encoders
├─ tests/
│  ├─ test_api.py       # API endpoint tests
│  └─ test_schemas.py   # Schema validation tests
├─ requirements.txt     # Project dependencies
└─ README.md            # This file
```

---

## Setup Instructions

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Manishrajmss13/credit-risk-api.git
cd credit-risk-api
```

### Step 2: Create and Activate Virtual Environment

#### Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `scikit-learn` - ML algorithms
- `pandas` - Data processing
- `joblib` - Model serialization
- `pytest` - Testing framework

### Step 4: Train the Model (Optional)

If you want to retrain the Random Forest model:

```bash
python model/train.py
```

This will:
- Load and preprocess the dataset
- Train the Random Forest classifier
- Save the model to `model/artifacts/`
- Generate evaluation metrics

### Step 5: Run the API

```bash
uvicorn app.main:app --reload
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Step 6: Verify the Setup

Open your browser and navigate to:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### Health Check Endpoint

#### GET `/`

Returns API status.

**Response:**
```json
{
  "message": "Credit Risk Prediction API is running!"
}
```

---

### POST /predict

Predict credit risk for a client based on their financial profile.

**Request Body:**
```json
{
  "laufkont": 1,
  "laufzeit": 24,
  "moral": 2,
  "verw": 4,
  "hoehe": 1000,
  "sparkont": 1,
  "beszeit": 3,
  "rate": 4,
  "famges": 2,
  "buerge": 1,
  "wohnzeit": 4,
  "verm": 1,
  "alter": 35,
  "weitkred": 1,
  "wohn": 2,
  "bishkred": 1,
  "beruf": 2,
  "pers": 2,
  "telef": 1,
  "gastarb": 2
}
```

**Response (Success - 200):**
```json
{
  "prediction": "good",
  "probability": 0.85,
  "confidence": "high"
}
```

**Response (Error - 422):**
```json
{
  "detail": [
    {
      "loc": ["body", "alter"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error"
    }
  ]
}
```

---

## Testing with Postman

### Step 1: Import API Collection

1. Open **Postman**
2. Click **Collections** → **Import**
3. Copy the API URL: `http://127.0.0.1:8000`

### Step 2: Create a POST Request

1. Create a new request
2. Set method to **POST**
3. URL: `http://127.0.0.1:8000/predict`
4. Go to **Body** tab
5. Select **raw** → **JSON**
6. Paste the request example above
7. Click **Send**

### Step 3: View Results

The response will show:
- **prediction**: `"good"` or `"bad"`
- **probability**: Confidence score (0-1)
- **confidence**: Risk level (`"high"`, `"medium"`, `"low"`)

### Screenshots: Postman Testing

> **<img width="894" height="515" alt="image" src="https://github.com/user-attachments/assets/dcdf9f27-5ca9-4a92-b5bd-3a92de5b1f8e" />
**

> **<img width="778" height="164" alt="image" src="https://github.com/user-attachments/assets/983be43e-2952-446c-8987-edfadb1495cf" />
**

---

## Testing with Swagger UI

### Step 1: Access Swagger UI

Open your browser and go to:
```
http://127.0.0.1:8000/docs
```

### Step 2: Explore Endpoints

You'll see:
- **GET /**: Health check
- **POST /predict**: Credit risk prediction

### Step 3: Test the Predict Endpoint

1. Click on **POST /predict**
2. Click **Try it out**
3. Modify the request body with your test data
4. Click **Execute**
5. View the response

### Screenshots: Swagger UI Documentation

> **<img width="1185" height="605" alt="image" src="https://github.com/user-attachments/assets/e7526c17-d4d8-4d82-b500-84b778a33018" />
**

> **<img width="1266" height="581" alt="image" src="https://github.com/user-attachments/assets/08d7e018-086d-4dfc-82ad-e4639d543216" />
**


> **<img width="1290" height="410" alt="image" src="https://github.com/user-attachments/assets/2ea5cd21-bdcc-45ce-a7bb-ee3cf4ec2c31" />
**

---

## Feature Importance

The Random Forest model ranks features by their importance in predicting credit risk:

### Top Features (Example Rankings):

| Rank | Feature | Importance | Contribution |
|------|---------|------------|--------------|
| 1 | `hoehe` | 0.18 | Loan amount is the strongest predictor |
| 2 | `laufzeit` | 0.15 | Duration affects risk assessment |
| 3 | `alter` | 0.12 | Age is a significant factor |
| 4 | `moral` | 0.11 | Credit history is important |
| 5 | `rate` | 0.10 | Installment rate matters |
| ... | ... | ... | ... |

### How to Generate Feature Importance Report

```bash
python model/train.py
```

The model training script outputs feature importance rankings and generates visualizations saved in `model/artifacts/`.



---



## Notes

- **Strict Validation:** The API validates all 20 input features; missing or invalid data returns descriptive validation errors
- **Feature Requirements:** All features must be provided; partial predictions are not supported
- **Probability Ranges:** Prediction probability is between 0 and 1 (0% to 100% confidence)
- **Modular Design:** Easy to swap Random Forest for other models (XGBoost, LightGBM, etc.)
- **Production Ready:** Includes error handling, logging, and unit tests

---

## Troubleshooting

### Issue: ModuleNotFoundError when running the API

**Solution:**
```bash
# Ensure virtual environment is activated
.\venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Port 8000 already in use

**Solution:**
```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

### Issue: Model file not found

**Solution:**
```bash
# Retrain the model
python model/train.py
```

---

## Running Tests

Execute unit tests to validate functionality:

```bash
pytest tests/ -v
```

This runs:
- `test_api.py` - API endpoint tests
- `test_schemas.py` - Request schema validation tests

---

## Project Roadmap (Future work)

- [ ] Add authentication (JWT tokens)
- [ ] Implement model versioning
- [ ] Add batch prediction endpoint
- [ ] Create Docker support
- [ ] Add database integration
- [ ] Deploy to cloud (AWS/GCP/Azure)

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact & Support

- **Author:** Manish Raj M S S
- **Email:** mssmanishraj@gmail.com
- **GitHub:** [@Manishrajmss13](https://github.com/Manishrajmss13)

For issues and questions, please open a [GitHub Issue](https://github.com/Manishrajmss13/credit-risk-api/issues).

---

**Last Updated:** February 2026

