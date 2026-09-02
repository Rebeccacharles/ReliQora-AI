import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="ReliQora-AI",
    page_icon="🛡️",
    layout="wide"
)


# Load model and scaler
model = joblib.load("models/logistic_regression.pkl")
scaler = joblib.load("models/scaler.pkl")


# App header
st.title("🛡️ ReliQora-AI")
st.subheader("AI-Powered Application Failure Prediction")

st.write(
    "Monitor application telemetry and estimate the probability "
    "of application failure."
)

st.divider()


# Telemetry input
st.header("📊 Application Telemetry")

left_col, right_col = st.columns(2)

with left_col:
    cpu = st.slider(
        "CPU Utilization (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

    memory = st.slider(
        "Memory Utilization (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

    disk = st.slider(
        "Disk Utilization (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

    request_rate = st.slider(
        "Request Rate",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

with right_col:
    response_latency = st.slider(
        "Response Latency (ms)",
        min_value=0.0,
        max_value=1000.0,
        value=200.0,
        step=10.0
    )

    error_rate = st.slider(
        "Error Rate (%)",
        min_value=0.0,
        max_value=20.0,
        value=2.0,
        step=0.5
    )

    network_latency = st.slider(
        "Network Latency (ms)",
        min_value=0.0,
        max_value=300.0,
        value=50.0,
        step=5.0
    )

    active_connections = st.slider(
        "Active Connections",
        min_value=0,
        max_value=1000,
        value=300,
        step=10
    )


# Build input dataframe in the same feature order used during training
input_data = pd.DataFrame(
    [[
        cpu,
        memory,
        disk,
        request_rate,
        response_latency,
        error_rate,
        network_latency,
        active_connections
    ]],
    columns=[
        "cpu_utilization",
        "memory_utilization",
        "disk_utilization",
        "request_rate",
        "response_latency",
        "error_rate",
        "network_latency",
        "active_connections"
    ]
)


# Apply the training scaler before prediction
scaled_input = scaler.transform(input_data)

# Keep feature names when passing the scaled data to the model
scaled_input = pd.DataFrame(
    scaled_input,
    columns=input_data.columns
)

failure_probability = model.predict_proba(scaled_input)[0][1]
failure_percentage = failure_probability * 100


# Classify the predicted risk
if failure_probability < 0.30:
    risk_level = "LOW"
    risk_message = "Application appears stable."
elif failure_probability < 0.60:
    risk_level = "MEDIUM"
    risk_message = "Application requires monitoring."
else:
    risk_level = "HIGH"
    risk_message = "Application may be at risk of failure."


# Display prediction
st.divider()
st.header("🚨 Failure Risk Prediction")

probability_col, risk_col, model_col = st.columns(3)

with probability_col:
    st.metric(
        "Failure Probability",
        f"{failure_percentage:.2f}%"
    )

with risk_col:
    st.metric(
        "Risk Level",
        risk_level
    )

with model_col:
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


# Check individual telemetry values for potential warning signs
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


st.divider()

st.caption(
    "ReliQora-AI | Application Health & Reliability"
)

