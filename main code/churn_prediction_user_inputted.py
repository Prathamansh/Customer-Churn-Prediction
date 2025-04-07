import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preprocess
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'].fillna(data['TotalCharges'].mean(), inplace=True)
data.drop('customerID', axis=1, inplace=True)

X = data.drop('Churn', axis=1)
y = data['Churn'].map({'Yes': 1, 'No': 0})
categorical_cols = X.select_dtypes(include=['object']).columns
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

# Feature importance
feature_names = pd.get_dummies(data.drop('Churn', axis=1), drop_first=True).columns
importance = pd.Series(model.feature_importances_, index=feature_names).sort_values(ascending=False)
print("Top 5 Features:")
print(importance.head())

# Interactive prediction
print(f"\nTest set contains {X_test.shape[0]} customers (index 0 to {X_test.shape[0] - 1})")
while True:
    try:
        # Ask user for customer index
        index = int(input("\nEnter the customer index to predict churn (or -1 to exit): "))
        
        # Exit condition
        if index == -1:
            print("Exiting...")
            break
        
        # Validate index
        if 0 <= index < X_test.shape[0]:
            # Get sample data for the customer
            sample = X_test[index].reshape(1, -1)
            prediction = model.predict(sample)[0]
            prob = model.predict_proba(sample)[0][1]  # Probability of churn (class 1)
            
            # Interpret prediction
            churn_status = "Churn" if prediction == 1 else "No Churn"
            print(f"Customer at index {index}:")
            print(f"Prediction: {churn_status}")
            print(f"Churn Probability: {prob:.2%}")
        else:
            print(f"Error: Index must be between 0 and {X_test.shape[0] - 1}")
    except ValueError:
        print("Error: Please enter a valid integer")