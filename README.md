# 📉 Customer Churn Prediction

This project builds a machine learning model to predict whether a telecom customer is likely to churn (stop using the service) based on demographic and usage data.  
It uses the Telco Customer Churn dataset and a Random Forest Classifier to classify customers as "Churn" or "No Churn" and provides churn probabilities.

---

## 🚀 Features

- **Data Preprocessing**: Handles missing values, encodes categorical variables, and scales numerical features.
- **Model**: Uses a Random Forest Classifier for binary classification.
- **Evaluation**: Reports accuracy, F1-score, and plots a confusion matrix.
- **Feature Importance**: Highlights key features influencing churn (e.g., tenure, monthly charges).
- **Interactive Prediction**: Users can input a test set index to predict churn and view the probability.

---

## 📁 Project Structure

CustomerChurnPrediction/ ├── main/ │ └── churn_prediction.py # Main script to run the model ├── churn_prediction.ipynb # Jupyter Notebook for exploration ├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset (user provides) └── README.md # Project documentation

yaml
Copy
Edit

---

## ✅ Requirements

- Python 3.6 or higher

### Required Libraries

- pandas  
- scikit-learn  
- matplotlib  
- seaborn

### Install Libraries

```bash
pip install pandas scikit-learn matplotlib seaborn
Or use a requirements.txt file:

txt
Copy
Edit
pandas
scikit-learn
matplotlib
seaborn
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📥 Dataset
Download the dataset from Kaggle and place the file in the project root:

Copy
Edit
WA_Fn-UseC_-Telco-Customer-Churn.csv
▶️ How to Run
Navigate to the project directory and run the script:

bash
Copy
Edit
python main/churn_prediction.py
🖥️ Script Output
Displays Accuracy, F1-score, and a Confusion Matrix plot.

Lists top 5 important features influencing churn.

Interactive prediction for test customers.

Example Output:
yaml
Copy
Edit
Accuracy: 0.7984
F1-Score: 0.5538

Top 5 Features:
tenure                0.1712
MonthlyCharges        0.1403
TotalCharges          0.1309
Contract_Two year     0.0701
Contract_One year     0.0502

Test set contains 1409 customers (index 0 to 1408)

Enter the customer index to predict churn (or -1 to exit): 0
Customer at index 0:
Prediction: No Churn
Churn Probability: 12.34%
📊 Model Performance
Dataset size: 7,043 customers

Test set size: 1,409 customers (20%)

Accuracy: ~78% – 82%

F1-score: ~0.50 – 0.60 (due to class imbalance)

💡 Possible Improvements
Use SMOTE for class balancing:

bash
Copy
Edit
pip install imbalanced-learn
Try advanced models like XGBoost:

bash
Copy
Edit
pip install xgboost
Deploy the model using Flask or FastAPI.

🧪 Troubleshooting
FileNotFoundError: Ensure the dataset CSV is in the root directory.

ModuleNotFoundError: Make sure all libraries are installed.

Invalid Input: Input must be an integer between 0 and 1408.

📜 License
This project is licensed under the MIT License.
