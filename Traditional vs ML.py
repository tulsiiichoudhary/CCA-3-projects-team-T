# Name: Subham Sahu 
# PRN: 1302250465
# Task: Traditional Programming vs ML Programming from Excel Input

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Read input from Excel file
excel_file = "Loan approval data.xlsx"
df = pd.read_excel(excel_file)
print("Member 1 Branch - Data Loaded:")
print(df.head())

X = df[["Income", "Credit_Score", "Existing_Loan"]]
y = df["Approved"]

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# Rule Logic updated for higher risk threshold
def traditional_rules(income, credit_score, existing_loan):
    if income >= 55000 and credit_score >= 710 and existing_loan <= 15000:
        return "Approved (Traditional Rule)"
    return "Rejected (Traditional Rule)"

test_profile = [[58000, 720, 14000]]
ml_decision = model.predict(test_profile)[0]
ml_result = "Approved (ML)" if ml_decision == 1 else "Rejected (ML)"
trad_result = traditional_rules(58000, 720, 14000)

print(f"Traditional Decision : {trad_result}")
print(f"ML Decision          : {ml_result}")
