import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib
import os

# -----------------------
# Load RFM
# -----------------------

rfm = pd.read_csv("data/processed/rfm_data.csv")

# Remove Customer ID for clustering
X = rfm.drop(columns=["Customer ID"])

# -----------------------
# Scale Data
# -----------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Save scaler
os.makedirs("models", exist_ok=True)
joblib.dump(scaler, "models/rfm_scaler.pkl")

print("Scaler Saved!")

# -----------------------
# Elbow Method
# -----------------------

wcss = []

for i in range(2, 11):

    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    wcss.append(model.inertia_) 

plt.figure(figsize=(8,5))

plt.plot(range(2,11), wcss, marker="o")

plt.title("Elbow Method")

plt.xlabel("Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.savefig("reports/elbow_method.png")

print("Elbow Chart Saved!")

# -----------------------
# Train Final Model
# -----------------------

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(X_scaled)

joblib.dump(kmeans, "models/kmeans.pkl")

print("Model Saved!")

# -----------------------
# Silhouette Score
# -----------------------

score = silhouette_score(X_scaled, rfm["Cluster"])

print(f"Silhouette Score : {score:.3f}")

# -----------------------
# Cluster Summary
# -----------------------

summary = rfm.groupby("Cluster").mean()

print("\nCluster Summary\n")

print(summary)

rfm.to_csv(
    "data/processed/customer_segments.csv",
    index=False
)

print("\nCustomer Segments Saved!")