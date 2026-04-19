
# Step 1: Import dependencies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Step 2: Load the dataset

data = pd.read_csv(r'C:\Users\MITRO\Downloads\Phishing_Legitimate_full.csv')

print("First 5 rows:")
print(data.head())


# Step 3: Dataset analysis

print("\nDataset Info:")
print(data.info())

print("\nDataset Description:")
print(data.describe())

print("\nMaximum values:")
print(data.max(axis=0))

data.drop("id", axis=1, inplace=True)

print("\nAfter removing ID column:")
print(data.head())

data['CLASS_LABEL'].hist()
plt.title('Class Distribution (0=Safe, 1=Phishing)')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()


# Step 4: Splitting data

x = data.drop("CLASS_LABEL", axis=1)
y = data["CLASS_LABEL"]

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

print(f"\nTest set shape: {x_test.shape}")
# Output: (2500, 48)


# Step 5: Training Random Forest Algorithm

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()

print("\nTraining model...")
rfc.fit(x_train, y_train)

print("Making predictions...")
preds = rfc.predict(x_test)

# Step 6: Model evaluation metrics

manual_accuracy = sum(preds == y_test.values) / len(preds)
print(f"\nManual Accuracy: {manual_accuracy}")
# Output: 0.984

from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy = accuracy_score(y_test, preds)
precision = precision_score(y_test, preds)
recall = recall_score(y_test, preds)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

print("\n PROJECT COMPLETE!")