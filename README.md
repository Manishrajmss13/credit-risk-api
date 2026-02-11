# Credit Risk Prediction API

A FastAPI-based project for predicting credit risk using a structured dataset of client financial and personal information. This project demonstrates end-to-end data processing, model integration, and a REST API deployment.

---

## Dataset

- **Source:** Public credit dataset (German credit-like dataset)  
- **Description:** Contains 1000+ entries of clients with features describing financial status, personal information, and loan details.  
- **Target Variable:** Credit risk classification (`good` / `bad`).  

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


## Methods

1. **Data Validation:** Uses Pydantic schemas to validate incoming JSON requests.  
2. **Model Prediction:** ML model loaded with joblib; predicts risk for input data.  
3. **API Endpoints:**  
   - `POST /predict` – accepts JSON payload with client features and returns credit risk prediction.  

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Manishrajmss13/credit-risk-api.git
cd credit-risk-api
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

### 5. Test Endpoints

Open http://127.0.0.1:8000/docs in your browser for Swagger UI.

Use the `/predict` endpoint to test predictions.

---

## API Endpoints

### POST /predict

**Request Example:**
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

**Response Example:**
```json
{
  "prediction": "good",
  "probability": 0.85
}
```

---

## Notes

- The API validates all input features strictly; missing or invalid data will return descriptive errors.
- Designed to be modular and extendable for other ML models.
- Ensure all 20 features are provided in the prediction request.

---

## License

This project is open source and available under the [MIT License](LICENSE).
