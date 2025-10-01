from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# Dataset with features and defect status (1: Defect, 0: No Defect)
data = {
    "LinesChanged": [10, 200, 50, 300],
    "Complexity": [5, 20, 10, 30],
    "BugFixCommit": [0, 1, 0, 1],
    "Defect": [0, 1, 0, 1]
}
df = pd.DataFrame(data)

# Split data into training and testing sets
X = df[["LinesChanged", "Complexity", "BugFixCommit"]]
y = df["Defect"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train ML model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Predict on new data
new_code_changes = [[100, 15, 0]]  # Example: New commit details
prediction = model.predict(new_code_changes)
print("Defect Prediction:", prediction)