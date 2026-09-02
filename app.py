import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="ReliQora-AI",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Load trained model and scaler
# --------------------------------------------------

model = joblib.load("models/logistic_regression.pkl")
scaler = joblib.load("models/scaler.pkl")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ ReliQora-AI")
st.subheader("AI-Powered Application Failure Prediction")

st.write(
    "Monitor application telemetry and predict the probability "
    "of application failure."
)

st.divider()

# --------------------------------------------------
# Telemetry Inputs
# --------------------------------------------------

st.header("📊 Application Telemetry")

col1, col2 = st.columns(2)

with col1:
    cpu = st.slider(
        "CPU Utilization (%)",
        0.0, 100.0, 50.0, 1.0
    )

    memory = st.slider(
        "Memory Utilization (%)",
        0.0, 100.0, 50.0, 1.0
    )

    disk = st.slider(
        "Disk Utilization (%)",
        0.0, 100.0, 50.0, 1.0
    )

    request_rate = st.slider(
        "Request Rate",
        0.0, 100.0, 50.0, 1.0
    )

with col2:
    response_latency = st.slider(
        "Response Latency (ms)",
        0.0, 1000.0, 200.0, 10.0
    )

    error_rate = st.slider(
        "Error Rate (%)",
        0.0, 20.0, 2.0, 0.5
    )

    network_latency = st.slider(
        "Network Latency (ms)",
        0.0, 300.0, 50.0, 5.0
    )

    active_connections = st.slider(
        "Active Connections",
        0, 1000, 300, 10
    )

# --------------------------------------------------
# Prepare input for ML model
# --------------------------------------------------

input_data = pd.DataFrame([[
    cpu,
    memory,
    disk,
    request_rate,
    response_latency,
    error_rate,
    network_latency,
    active_connections
]], columns=[
    "cpu_utilization",
    "memory_utilization",
    "disk_utilization",
    "request_rate",
    "response_latency",
    "error_rate",
    "network_latency",
    "active_connections"
])

# Scale input using the same scaler used during training
scaled_input = scaler.transform(input_data)

# Predict failure probability
failure_probability = model.predict_proba(scaled_input)[0][1]

# Convert to percentage
failure_percentage = failure_probability * 100

# --------------------------------------------------
# Determine risk level
# --------------------------------------------------

if failure_probability < 0.30:
    risk_level = "LOW"
    risk_message = "Application appears stable."
elif failure_probability < 0.60:
    risk_level = "MEDIUM"
    risk_message = "Application requires monitoring."
else:
    risk_level = "HIGH"
    risk_message = "Application may be at risk of failure."

# --------------------------------------------------
# Prediction Results
# --------------------------------------------------

st.divider()

st.header("🚨 Failure Risk Prediction")

result_col1, result_col2, result_col3 = st.columns(3)

with result_col1:
    st.metric(
        "Failure Probability",
        f"{failure_percentage:.2f}%"
    )

with result_col2:
    st.metric(
        "Risk Level",
        risk_level
    )

with result_col3:
    st.metric(
        "Model",
        "Logistic Regression"
    )

if risk_level == "LOW":
    st.success(f"🟢 {risk_message}")

elif risk_level == "MEDIUM":
    st.warning(f"🟡 {risk_message}")

else:
    st.error(f"🔴 {risk_message}")

# --------------------------------------------------
# Risk Indicators
# --------------------------------------------------

st.header("🔎 Key Risk Indicators")

risk_indicators = []

if cpu >= 80:
    risk_indicators.append("High CPU utilization")

if memory >= 80:
    risk_indicators.append("High memory utilization")

if disk >= 80:
    risk_indicators.append("High disk utilization")

if response_latency >= 500:
    risk_indicators.append("High response latency")

if error_rate >= 10:
    risk_indicators.append("High error rate")

if network_latency >= 150:
    risk_indicators.append("High network latency")

if active_connections >= 700:
    risk_indicators.append("High number of active connections")

if risk_indicators:
    for indicator in risk_indicators:
        st.warning(f"⚠️ {indicator}")
else:
    st.success("✅ No major telemetry risk indicators detected.")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "ReliQora-AI | Predictive Application Failure Detection "
    "using Machine Learning"
)