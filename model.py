import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv('cholesterol_data.csv')

# Select features and target
X = df[['age', 'bmi', 'blood_pressure', 'activity_level']]
y = df['cholesterol_level']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

def predict_cholesterol(age, bmi, blood_pressure, activity_level):
    # Load model and scaler
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')

    # Prepare input
    input_data = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'blood_pressure': blood_pressure,
        'activity_level': activity_level
    }])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    return round(prediction[0], 2)
