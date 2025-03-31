import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Load the model
model = joblib.load("app/model/best_titanic_model.pkl")

# Load the scaler and label encoders
scaler = joblib.load("app/model/scaler.pkl")
label_encoders = joblib.load("app/model/label_encoders.pkl")

def preprocess_data(data):
    # Convert data to DataFrame
    df = pd.DataFrame([data], columns=['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Embarked'])

    # Apply label encoding
    df['Sex'] = label_encoders['Sex'].transform([df['Sex'][0]])[0]
    df['Embarked'] = label_encoders['Embarked'].transform([df['Embarked'][0]])[0]

    # Create FamilySize feature
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # Apply scaling
    numerical_features = ['Age', 'Fare', 'FamilySize']
    df[numerical_features] = scaler.transform(df[numerical_features])

    # Ensure the order of columns matches the training data
    df = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Embarked', 'FamilySize']]

    return df.values


def predict(data):
    processed_data = preprocess_data(data)
    prob = model.predict_proba(processed_data)[0]  # Get probability of survival
    prediction = int(np.argmax(prob))  # 0 or 1
    return {"prediction": prediction, "probability": prob.tolist()}
