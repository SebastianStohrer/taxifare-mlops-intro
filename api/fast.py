########################
#
# FastAPI server to serve the model
#
#########################

import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"greeting": "Hello"}

@app.get("/predict")
def predict():
    """Dummy endpoint, returns a random fare until a real model is wired in"""
    return {"fare": round(random.uniform(5, 50), 2)}
