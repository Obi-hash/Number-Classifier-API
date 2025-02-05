from fastapi import FastAPI, Query, Response, status
import json
import math

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def get_fun_fact(n):
    if is_armstrong(n):
        digits = [int(d) for d in str(abs(n))]
        power = len(digits)
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^{power}" for d in digits) + f" = {abs(n)}"
    return "No special fun fact available."

@app.get("/api/classify-number")
def classify_number(number: str = Query(...)):
    try:
        # Try to convert the input to a float first, then check if it's an integer
        number_float = float(number)
        number_int = int(number_float) if number_float.is_integer() else None
    except ValueError:
        # If conversion fails, return a 400 Bad Request with the required JSON format
        return Response(
            content=json.dumps({"number": number, "error": True}, indent=4),
            media_type="application/json",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    # Handle negative and floating-point numbers
    if number_int is not None:
        number_to_check = number_int
    else:
        number_to_check = number_float

    properties = []
    if is_armstrong(number_to_check):
        properties.append("armstrong")
    properties.append("even" if number_to_check % 2 == 0 else "odd")

    result = {
        "number": number_to_check,
        "is_prime": is_prime(number_to_check) if isinstance(number_to_check, int) else False,
        "is_perfect": is_perfect(number_to_check) if isinstance(number_to_check, int) else False,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(number_to_check))),
        "fun_fact": get_fun_fact(number_to_check)
    }

    return Response(
        content=json.dumps(result, indent=4),  # Ensure pretty-printing
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )
