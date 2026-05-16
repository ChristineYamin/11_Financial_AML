import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# --- 1. THE ASSET LOADER (The Memory) ---
@st.cache_resource
def load_assets():
    model = joblib.load('C:/Projects/11_Financial_AML/model/aml_xgb_model.pkl')
    cols = joblib.load('C:/Projects/11_Financial_AML/model/model_columns.pkl')
    return model, cols

model, model_columns = load_assets()

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="FinGuard AML", page_icon="🛡️", layout="wide")


# --- 2. SCENARIO SIMULATOR (The UI Helper) ---
with st.sidebar:
    st.header("💡 Quick Scenarios")
    st.write("Use these to test the model instantly.")
    if st.button("Load Suspicious Transfer"):
        st.session_state.amt = 100000
        st.session_state.old_o = 100000
        st.session_state.new_o = 0
        st.session_state.type = "TRANSFER"
    
    if st.button("Load Normal Activity"):
        st.session_state.amt = 500
        st.session_state.old_o = 2500
        st.session_state.new_o = 2000
        st.session_state.type = "CASH_OUT"
    
    st.divider()
    st.header("⚙️ Settings")
    if st.button("Reset Form"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()


# --- 3. THE UI INTERFACE ---
st.title("🛡️ Financial AML Intelligence")
st.markdown("##### Project 11: Enterprise Anti-Money Laundering Detection Engine")
st.divider()

col1, col2 = st.columns(2)

with col1:
    amt = st.number_input("Transaction Amount ($)", min_value=0, step=100, key="amt", value=st.session_state.get('amt', 1000))
    old_o = st.number_input("Sender Initial Balance", min_value=0, step=500, key="old_o", value=st.session_state.get('old_o', 5000))
    new_o = st.number_input("Sender Final Balance", min_value=0, step=500, key="new_o", value=st.session_state.get('new_o', 4000))

with col2:
    t_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT"], key="type")
    old_d = st.number_input("Receiver Initial Balance", min_value=0, step=500)
    new_d = st.number_input("Receiver Final Balance", min_value=0, step=500)

# --- 4. THE FEATURE ENGINEER & PREDICTOR ---
if st.button("Analyze Transaction", use_container_width=True):
    if amt <= 0:
        st.error("Please enter a valid transaction amount.")
    else:
        # Math Layer (Feature Engineering)
        err_o = new_o + amt - old_o
        err_d = old_d + amt - new_d
        
        # Prepare Data for Model
        input_df = pd.DataFrame({
            'amount': [amt], 'oldbalanceOrg': [old_o], 'newbalanceOrig': [new_o],
            'oldbalanceDest': [old_d], 'newbalanceDest': [new_d],
            'errorBalanceOrig': [err_o], 'errorBalanceDest': [err_d],
            'hour': [datetime.now().hour], 
            'type_TRANSFER': [1 if t_type == "TRANSFER" else 0]
        })[model_columns]
        
        # Prediction logic
        prob = model.predict_proba(input_df)[0][1]
        st.markdown("### Analysis Result")
        if prob > 0.5:
            st.error(f"🚨 **FRAUD DETECTED**")
            st.metric("Risk Probability", f"{prob*100:.2f}%")
        else:
            st.success(f"✅ **LEGITIMATE TRANSACTION**")
            st.metric("Risk Probability", f"{prob*100:.4f}%")

st.divider()
st.caption("Developed by Christine | 23 Projects at 23")
