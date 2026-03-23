from fastapi import FastAPI
import string
import random



app = FastAPI()


@app.get("/password")
def generate_password(length:int = 8):

    if length <= 0:
        return {"message":"Password length can't be negative or zero !"}
    
    if length > 20:
        return {"message":"Password length can't be more than 30 !"}
    
    alphabets = string.ascii_letters
    numbers = string.digits
    extra = "!@#$%^&*" * 2

    combination = list(alphabets + numbers + extra)
    random.shuffle(combination)
    password = ""

    for i in range(length):
        password += random.choice(combination)
    
    password = list(password)
    random.shuffle(password)
   
    password = "".join(password)
    return {"password":password}
