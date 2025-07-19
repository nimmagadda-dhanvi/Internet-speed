# app.py
import streamlit as st
import speedtest

# Set up page config
st.set_page_config(page_title="Internet Speed Checker",  layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #ffffff;  /* White page background */
            color: #000000;             /* Black text */
        }

        .main {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid #2196f3;  /* Blue border */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
        }

        .status {
            font-size: 24px;
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }

        .online {
            background-color: #4caf50;
            color: white;
        }

        .offline {
            background-color: #f44336;
            color: white;
        }

        .stButton {
            display: flex;
            justify-content: center;
            margin-top: 25px;  /* Push the button down */
        }

        .stButton>button {
            background-color: #2196f3;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            border: none;
        }

        .stButton>button:hover {
            background-color: #1976d2;
        }
    </style>
""", unsafe_allow_html=True)

# Main title box
st.markdown('<div class="main"><h1>Internet Speed Checker</h1>', unsafe_allow_html=True)

# Speed check logic
if st.button("Check Speed"):
    st.write("Running speed test... Please wait ⏳")
    wifi = speedtest.Speedtest()
    download = round(wifi.download() / 1_000_000, 2)
    upload = round(wifi.upload() / 1_000_000, 2)

    st.markdown(f'<p class="status online">Status: Online</p>', unsafe_allow_html=True)
    st.success(f"📥 Download Speed: {download} Mbps")
    st.success(f"📤 Upload Speed: {upload} Mbps")
else:
    st.markdown(f'<p class="status offline">Status: Unknown (Click button)</p>', unsafe_allow_html=True)

# Close box
st.markdown('</div>', unsafe_allow_html=True)
