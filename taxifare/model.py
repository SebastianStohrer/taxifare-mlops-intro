from pathlib import Path

import joblib

def load_model(model_path: str ):
    """
    Load a trained model or pipeline from disk and returns
    loaded model.
    """
    return joblib.load(model_path)

def predict(model, data):
    """
    Generate predictions using a loaded model.
    """
    return model.predict(data)
