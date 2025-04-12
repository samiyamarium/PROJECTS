import streamlit as st
from sklearn.linear_model import LinearRegression
import joblib

# Example training data (you can replace with real data)
X = [[1], [2], [3], [4], [5]]   # Features
y = [3, 6, 9, 12, 15]           # Targets (y = 3 * x)

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a .pkl file
joblib.dump(model, 'linear_regression_model.pkl')

print("Model saved as 'linear_regression_model.pkl'")

model=joblib.load("linear_regression_model.pkl")
st.title("Linear Regression prediction app")
st.write("Enter the feature value to get a prediction")

feature_value=st.number_input("Enter a value for the feature : ",min_value=0, max_value=12)

if st.button("Predict :rosette:"):
    #prediction=model.predict([[feature_value]])
    st.write(f"The prediction target value is {model.predict([[feature_value]])}")


