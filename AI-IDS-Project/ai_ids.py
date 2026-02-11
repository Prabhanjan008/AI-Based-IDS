import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Step 1: Generate Normal Traffic
np.random.seed(42)
normal_traffic = np.random.normal(50, 5, 200)

# Step 2: Generate Attack Traffic
attack_traffic = np.random.normal(100, 10, 20)

# Combine Data
data = np.concatenate([normal_traffic, attack_traffic])
df = pd.DataFrame(data, columns=["packet_size"])

# Step 3: Train AI Model
model = IsolationForest(contamination=0.1)
model.fit(df)

# Step 4: Predict anomalies
df["anomaly"] = model.predict(df)

# Show detected attacks
print("Detected Suspicious Traffic:\n")
print("\n⚠️ ALERT: Suspicious Network Activity Detected!\n")
print(df[df["anomaly"] == -1])



# Step 5: Plot graph
plt.scatter(df.index, df["packet_size"], c=df["anomaly"])
plt.title("AI-Based IDS Detection")
plt.xlabel("Packet Number")
plt.ylabel("Packet Size")
plt.show()
