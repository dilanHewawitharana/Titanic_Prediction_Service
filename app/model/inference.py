import joblib
import numpy as np

model = joblib.load("app/model/best_titanic_model.pkl")

def predict(data):
    prob = model.predict_proba([data])[0]  # Get probability of survival
    prediction = int(np.argmax(prob))  # 0 or 1
    return {"prediction": prediction, "probability": prob.tolist()}