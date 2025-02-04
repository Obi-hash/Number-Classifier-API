from fastapi import FastAPI, Query, Response, status
import json

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    if is_armstrong(n):
        digits = [int(d) for d in str(n)]
        power = len(digits)
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^{power}" for d in digits) + f" = {n}"
    return "No special fun fact available."

@app.get("/api/classify-number")
def classify_number(number: str = Query(...)):
    try:
        number_int = int(number)
    except ValueError:
        # Return the error response with the required format
        return Response(
            content=json.dumps({"number": number, "error": True}, indent=4),  # Include the number field
            media_type="application/json",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    properties = ["armstrong"] if is_armstrong(number_int) else []
    properties.append("even" if number_int % 2 == 0 else "odd")

    result = {
        "number": number_int,
        "is_prime": is_prime(number_int),
        "is_perfect": is_perfect(number_int),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number_int)),
        "fun_fact": get_fun_fact(number_int)
    }

    return Response(
        content=json.dumps(result, indent=4),  # Ensure pretty-printing
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )
