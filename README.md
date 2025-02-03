# Number Classifier API

A simple API that classifies numbers based on mathematical properties.

## 🚀 Features
- Check if a number is **prime, perfect, or an Armstrong number**.
- Returns **fun facts** about numbers using Numbers API.
- Hosted on a **public API endpoint**.

## 📌 API Endpoint
**GET** `/api/classify-number?number=371`

### ✅ Sample Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

