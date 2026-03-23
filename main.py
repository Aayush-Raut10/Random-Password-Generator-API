from fastapi import FastAPI
import string
import random
SPECIAL_SYMBOLS = string.punctuation


app = FastAPI()


@app.get("/generate_password")
def generate_password(length:int = 8):

    if length <= 0:
        return {"message":"Password length can't be negative or zero !"}
    
    if length > 500:
        return {"message":"Password length can't be more than 500 !"}
    
    alphabets = string.ascii_letters
    numbers = string.digits
    extra = SPECIAL_SYMBOLS

    combination = list(alphabets + numbers + extra)
    random.shuffle(combination)
    password = ""

    for i in range(length):
        password += random.choice(combination)
    
    password = list(password)
    random.shuffle(password)
   
    password = "".join(password)
    return {"password":password}


@app.post("/check_password")
def is_password_strong(payload:dict):
    password = payload.get("password").strip()
    
    if not password:
        return {"status": "password is not provided"}
    
    issues = []
    
    if len(password) < 8:
        issues.append("Password is less than 8 characters")

    if not (any(char.isdigit() for char in password)):
        issues.append("Missing digits")

    if not (any(char.islower() for char in password)):
        issues.append("Missing lowercase")
    
    if not any(c.isupper() for c in password):
        issues.append("Missing uppercase")

    if not any(char in SPECIAL_SYMBOLS for char in password):
        issues.append("Missing special symbols")

    if issues:
        return {"is_strongest": False, "issues":issues}
    
    return {"is_strongest": True}