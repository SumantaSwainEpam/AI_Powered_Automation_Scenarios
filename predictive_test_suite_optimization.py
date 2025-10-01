import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Historical Data
data = {
    "TestCaseID": [1, 2, 3, 4],
    "ExecutionTime": [10, 15, 5, 20],
    "FailedBefore": [1, 0, 1, 0],
    "ChangedModules": [2, 3, 1, 4],
    "Priority": [1, 1, 1, 0]
}
df = pd.DataFrame(data)

# Train a classifier
features = df[["ExecutionTime", "FailedBefore", "ChangedModules"]]
labels = df["Priority"]
clf = RandomForestClassifier()
clf.fit(features, labels)

# Predict Priority Scores for New Tests
new_test_cases = pd.DataFrame({"ExecutionTime": [12], "FailedBefore": [1], "ChangedModules": [3]})
predicted_priority = clf.predict_proba(new_test_cases)[:, 1]  # Probabilities for high-priority
print("Predicted Priority:", predicted_priority)