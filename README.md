# Number Classification API

## Description  
This API takes a number as input and returns interesting mathematical properties along with a fun fact.  

## API Specification  
- **Endpoint:** `GET /api/classify-number?number=371`
- **Example Response (200 OK):**  
  ```json
  {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }

    Example Response (400 Bad Request):
  {
  "number": "alphabet",
  "error": true
  }

Requirements

  Technology Stack: Python, Flask

  Must be deployed to a publicly accessible endpoint

  Must handle CORS

  Must return responses in JSON format

  Version Control:
  
     Hosted on GitHub
     Public repository with a structured README

Setup Instructions

  1. Clone the repository:

       git clone https://github.com/Obi-hash/number-classifier-api.git
       cd number-classifier-api

  2. Install dependencies:

       pip install -r requirements.txt

  3. Run the API locally:

       python main.py

  4. Deploy to Render or another cloud service.

  Deployment

     To deploy the API, follow the instructions for Render or another cloud provider.

  Contribution

     Feel free to contribute! Fork the repo, make your changes, and submit a pull request.

  License
 
    MIT License.
  


