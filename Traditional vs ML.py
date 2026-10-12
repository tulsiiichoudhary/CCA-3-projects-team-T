# Name: Nitya Juneja
# PRN: 1302250494
# Task: Traditional vs ML - Boundary Condition Analysis

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

excel_file = "Loan approval data.xlsx"
df = pd.read_excel(excel_file)

X = df[["Income", "Credit_Score", "Existing_Loan"]]
y = df["Approved"]

model = DecisionTreeClassifier(max_depth=3, random_state=123)
model.fit(X, y)

def traditional_rules(income, credit_score, existing_loan):
    if income > 50000 and credit_score > 720 and existing_loan < 10000:
        return "Instant Approval (Traditional Rule)"
    return "Manual Review (Traditional Rule)"

applicant = [[52000, 725, 8000]]
ml_res = "Approved (ML)" if model.predict(applicant)[0] == 1 else "Rejected (ML)"
trad_res = traditional_rules(52000, 725, 8000)

print(f"Traditional Decision : {trad_res}")
print(f"ML Decision          : {ml_res}")
