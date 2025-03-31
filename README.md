# Titanic_Prediction_Service

## Overview
The Titanic Prediction Service predicts survival probabilities using passenger features. It offers both synchronous and asynchronous API endpoints built with FastAPI. The backend consists of a pre-trained LightGBM model for predictions, and the service supports containerized deployment using Docker.

You can download and contribute to this project on GitHub:  
[GitHub Repository](https://github.com/dilanHewawitharana/Titanic_Prediction_Service)

## Project Structure
```
TITANIC_PREDICTION_SERVICE/
│── train_model/
│   ├── model_training.ipynb
│── titanic/
│   ├── test.csv
│   ├── train.csv
│── app/
│   ├── model/
│   │   ├── best_titanic_model.pkl
│   │   ├── inference.py
│   ├── routes/
│   │   ├── async_routes.py
│   │   ├── sync_routes.py
│── main.py
│── Dockerfile
│── requirements.txt
```

## How to Set Up and Run

### Run the Service as a Docker Container
1. Clone the repository:
   ```sh
   git clone https://github.com/dilanHewawitharana/Titanic_Prediction_Service.git
   cd Titanic_Prediction_Service
   ```
2. Build the Docker Image:
   ```sh
   docker build -t titanic-prediction .
   ```
3. Run the Container:
   ```sh
   docker run -p 8000:8000 titanic-prediction
   ```
4. Open the FastAPI interface:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Run the Service Locally (for Development)
1. Clone the repository:
   ```sh
   git clone https://github.com/dilanHewawitharana/Titanic_Prediction_Service.git
   cd Titanic_Prediction_Service
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
4. Open the FastAPI interface:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

### Synchronous Prediction API
- **Endpoint:** `POST /titanic_sync`
- **Request Body:**
  ```json
    {\"data\": [3, \'male\', 22.0, 7.25, 0, 0, \'S\']}
  ```
- **Response:**
  ```json
  {"prediction": 0, "probability": 0.34}
  ```
- **Example:**
  ```sh
  curl -X POST http://127.0.0.1:8000/titanic_sync -H "Content-Type: application/json" -d "{\"data\": [3, \"male\", 22.0, 7.25, 0, 0, \"S\"]}"
  ```

### Asynchronous Prediction API
- **Endpoint:** `POST /titanic_async`
- **Request Body:**
  ```json
    {\"data\": [3, \"male\", 22.0, 7.25, 0, 0, \"S\"]}
  ```
- **Response:**
  ```json
  {"task_id": "123e4567-e89b-12d3-a456-426614174000"}
  ```
- **Example:**
  ```sh
  curl -X POST http://127.0.0.1:8000/titanic_async -H "Content-Type: application/json" -d "{\"data\": [3, \"male\", 22.0, 7.25, 0, 0, \"S\"]}"
  ```

### Get Async Result
- **Endpoint:** `GET /titanic_result/{task_id}`
- **Example:**
  ```sh
  curl -X GET http://127.0.0.1:8000/titanic_result/b778ade6-f91e-4ab7-bac5-474a82ef0617
  ```

## Model Training

The Titanic Prediction Service uses a pre-trained LightGBM model. The training process includes:
- Data preprocessing using pandas and scikit-learn
- Feature engineering and normalization
- Training a LightGBM classifier
- Evaluating model performance (accuracy, confusion matrix, and ROC curve)
- Saving the trained model as `best_titanic_model.pkl`

### Data Source
- [Titanic Dataset on Kaggle](https://www.kaggle.com/c/titanic)

## Conclusion
This project successfully implements a Titanic passenger survival prediction API with both synchronous and asynchronous endpoints. It is containerized with Docker for easy deployment and scalability.
