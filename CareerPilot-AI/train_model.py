import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. Load Dataset
# ============================================================

print("📂 Loading career dataset...")

data = pd.read_csv("data/careers.csv")

print(f"✅ Dataset loaded: {len(data)} records")


# ============================================================
# 2. Separate Features and Target
# ============================================================

X = data.drop("Career", axis=1)

y = data["Career"]


# ============================================================
# 3. Train/Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


print(f"📚 Training samples: {len(X_train)}")

print(f"🧪 Testing samples: {len(X_test)}")


# ============================================================
# 4. Create Model
# ============================================================

print("\n🤖 Training CareerPilot AI...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    max_depth=12
)


# ============================================================
# 5. Train
# ============================================================

model.fit(
    X_train,
    y_train
)

print("✅ Model training completed!")


# ============================================================
# 6. Predictions
# ============================================================

predictions = model.predict(X_test)


# ============================================================
# 7. Evaluation
# ============================================================

accuracy = accuracy_score(
    y_test,
    predictions
)


print("\n============================================")
print("           MODEL PERFORMANCE")
print("============================================")

print(
    f"🎯 Accuracy: {accuracy * 100:.2f}%"
)


print("\n📊 Classification Report:")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ============================================================
# 8. Save Model
# ============================================================

model_path = "model/career_model.pkl"

joblib.dump(
    model,
    model_path
)


print("\n============================================")
print("🎉 CareerPilot AI Model Saved!")
print("============================================")

print(
    f"📁 Location: {model_path}"
)