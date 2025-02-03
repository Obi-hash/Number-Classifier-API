from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Helper function to check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n


def get_fun_fact(n):
    # Check if the number is an Armstrong number
    if is_armstrong(n):
        return f"{n} is an Armstrong number because " + " + ".join([f"{int(d)}^{len(str(n))}" for d in str(n)]) + f" = {n}"

    # Fetch fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available")
    except:
        return "No fun fact available"

    return "No fun fact available"

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Enter an integer number")):
    try:
        # Check if number is prime, perfect, or armstrong
        prime_status = is_prime(number)
        perfect_status = is_perfect(number)
        armstrong_status = is_armstrong(number)

        # Determine odd or even
        parity = "even" if number % 2 == 0 else "odd"

        # Assign properties
        properties = [parity]
        if armstrong_status:
            properties.insert(0, "armstrong")

        # Calculate digit sum
        digit_sum = sum(int(digit) for digit in str(number))

        # Fetch a fun fact
        fun_fact = get_fun_fact(number)

        return {
            "number": number,
            "is_prime": prime_status,
            "is_perfect": perfect_status,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }

    except:
        return {"number": number, "error": True}

