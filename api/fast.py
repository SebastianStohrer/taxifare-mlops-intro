########################
#
# FastAPI server to serve the model
#
#########################

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"greeting": "Hello"}

@app.get("/predict")
def predict(
    pickup_datetime: str,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int,
):
    """No model yet — placeholder fare so we can validate input handling end-to-end"""
    return {"fare": passenger_count * 2.5}
