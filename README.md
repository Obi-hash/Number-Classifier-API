# Number Classification API

This is a FastAPI-based web service that classifies a given number and provides information such as whether it is prime, perfect, or an Armstrong number. It also includes a fun fact about the number.

## Features
- Classify a number as prime, perfect, or Armstrong.
- Check if the number is even or odd.
- Calculate the sum of the digits of the number.
- Fetch a fun fact about the number from an external API.

## Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-classification-api.git
   cd number-classification-api

### Install the dependencies
2. pip install -r requirements.txt

### Run the FastAPI server
3. uvicorn main:app --reload

### Open your browser and visit
4. http://127.0.0.1:8000/


API Endpoints

Root Endpoint

 GET /

   Returns a welcome message.

Number Classification Endpoint

  GET /api/classify-number?number=<integer>

   Classifies the given number and returns its properties.

   Example: http://127.0.0.1:8000/api/classify-number?number=371

Response:

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Handling

  400 Bad Request: If the input is not a valid integer.

   {
    "number": "alphabet",
    "error": true
   }
