# 📉 Customer Churn Prediction

This project builds a machine learning model to predict whether a telecom customer is likely to churn (stop using the service) based on demographic and usage data. It uses the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and a Random Forest Classifier to classify customers as "Churn" or "No Churn," providing churn probabilities.

---

## 🚀 Features

- **Data Preprocessing**: Handles missing values, encodes categorical variables, and scales numerical features.  
- **Model**: Utilizes a Random Forest Classifier for binary classification.  
- **Evaluation**: Reports accuracy, F1-score, and visualizes a confusion matrix.  
- **Feature Importance**: Identifies key factors influencing churn (e.g., tenure, monthly charges).  
- **Interactive Prediction**: Allows users to input a test set index to predict churn and view probabilities.

---

## 📁 Project Structure

CustomerChurnPrediction/
├── main/
│   └── churn_prediction.py       # Main script to run the model
├── churn_prediction.ipynb        # Jupyter Notebook for exploration
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset (user provides)
└── README.md                     # Project documentation

---

## ✅ Requirements

- **Python**: 3.6 or higher

### Required Libraries
- `pandas`  
- `scikit-learn`  
- `matplotlib`  
- `seaborn`

### Install Libraries

```pip install pandas scikit-learn matplotlib seaborn

 Dataset
Download the dataset from Kaggle and place it in the project root:
WA_Fn-UseC_-Telco-Customer-Churn.csv

 How to Run
Navigate to the project directory:
bash

cd CustomerChurnPrediction

Run the script:
bash

python main/churn_prediction.py

 Example Output

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

 License
This project is open-source and available under the MIT License.

