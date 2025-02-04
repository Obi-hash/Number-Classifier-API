from fastapi import FastAPI, Query, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "Fun fact unavailable."
    return "Fun fact unavailable."

@app.get("/api/classify-number")
def classify_number(number: str = Query(...)):
    try:
        # Try to convert the input to an integer
        number_int = int(number)
    except ValueError:
        # If conversion fails, return a 400 Bad Request with the required JSON format
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "number": number,
                "error": True
            }
        )

    properties = []
    if is_armstrong(number_int):
        properties.append("armstrong")
    properties.append("even" if number_int % 2 == 0 else "odd")

    # Custom fun fact for Armstrong numbers
    fun_fact = get_fun_fact(number_int)
    if is_armstrong(number_int):
        digits = [int(d) for d in str(number_int)]
        power = len(digits)
        armstrong_fact = f"{number_int} is an Armstrong number because " + " + ".join(f"{d}^{power}" for d in digits) + f" = {number_int}"
        fun_fact = armstrong_fact

    result = {
        "number": number_int,
        "is_prime": is_prime(number_int),
        "is_perfect": is_perfect(number_int),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number_int)),
        "fun_fact": fun_fact
    }
    return result

@app.get("/")
def root():
    return {"message": "Number Classification API is running!"}
