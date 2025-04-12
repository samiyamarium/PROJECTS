import streamlit as st
from cryptography.fernet import Fernet
import base64
import json
import os

DATA_FILE = "secure_data.json"

# ---------- Utility Functions ----------

def generate_key(passkey):
    """Generate a Fernet key from the user passkey."""
    return base64.urlsafe_b64encode(passkey.ljust(32).encode()[:32])

def save_data(encrypted_data, key):
    """Save encrypted data and key to a local JSON file."""
    data = {
        "encrypted_data": encrypted_data.decode(),
        "fernet_key": key.decode()
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    """Load encrypted data and key from local JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return None

# ---------- Session State Setup ----------
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "authorized" not in st.session_state:
    st.session_state.authorized = True

# ---------- Lockout (Fake Login) ----------
if not st.session_state.authorized:
    st.title("🔒 Reauthorization Required")
    password = st.text_input("Enter admin password to unlock:", type="password")
    if password == "admin123":
        st.session_state.failed_attempts = 0
        st.session_state.authorized = True
        st.success("Access granted.")
    else:
        st.warning("Incorrect password.")
    st.stop()

# ---------- Main UI ----------
st.title("🔐 Secure Data Encryption with JSON Storage")

tab1, tab2 = st.tabs(["Encrypt & Store Data", "Decrypt Data"])

with tab1:
    st.subheader("🔒 Encrypt and Store Data")
    data = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if data and passkey:
            key = generate_key(passkey)
            f = Fernet(key)
            encrypted = f.encrypt(data.encode())
            save_data(encrypted, key)
            st.success("Data encrypted and stored in secure_data.json.")
        else:
            st.warning("Please enter both data and a passkey.")

with tab2:
    st.subheader("🔓 Decrypt Stored Data")
    passkey_attempt = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        stored = load_data()
        if not stored:
            st.info("No data has been stored yet.")
        else:
            try:
                key = generate_key(passkey_attempt)
                if key.decode() != stored["fernet_key"]:
                    raise ValueError("Wrong key")

                f = Fernet(key)
                decrypted = f.decrypt(stored["encrypted_data"].encode()).decode()
                st.success("Data decrypted successfully!")
                st.code(decrypted)
                st.session_state.failed_attempts = 0
            except Exception:
                st.session_state.failed_attempts += 1
                st.error("Incorrect passkey.")
                if st.session_state.failed_attempts >= 3:
                    st.session_state.authorized = False
                    st.warning("Too many failed attempts. Please reauthorize.")
                    st.experimental_rerun()
