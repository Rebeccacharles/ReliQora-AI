import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
np.random.seed(42)

# Number of telemetry records
N = 10000

# Generate application telemetry
cpu_utilization = np.random.uniform(10, 100, N)
memory_utilization = np.random.uniform(20, 100, N)
disk_utilization = np.random.uniform(10, 100, N)
request_rate = np.random.uniform(50, 1000, N)
response_latency = np.random.uniform(20, 1000, N)
error_rate = np.random.uniform(0, 20, N)
network_latency = np.random.uniform(5, 300, N)
active_connections = np.random.randint(10, 1000, N)

# Create a risk score based on unhealthy telemetry conditions
risk_score = (
    0.20 * cpu_utilization
    + 0.20 * memory_utilization
    + 0.10 * disk_utilization
    + 0.10 * response_latency / 10
    + 0.15 * error_rate * 5
    + 0.10 * network_latency / 3
    + 0.15 * active_connections / 10
)

# Add some randomness
risk_score += np.random.normal(0, 10, N)

# Define application failure
failure = (risk_score > 55).astype(int)

# Create DataFrame
df = pd.DataFrame({
    "cpu_utilization": cpu_utilization,
    "memory_utilization": memory_utilization,
    "disk_utilization": disk_utilization,
    "request_rate": request_rate,
    "response_latency": response_latency,
    "error_rate": error_rate,
    "network_latency": network_latency,
    "active_connections": active_connections,
    "failure": failure
})

# Create output directory
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

# Save dataset
output_path = output_dir / "telemetry_data.csv"
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully!")
print(f"Shape: {df.shape}")
print(f"Saved to: {output_path}")
print("\nFailure distribution:")
print(df["failure"].value_counts())
