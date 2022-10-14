import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import Authenticate
from yaml import SafeLoader
import time

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="PM", page_icon=":hospital:", layout="wide")

from pms.login import init_authenticator

if __name__ == "__main__":
    authenticator, name, authentication_status, username = init_authenticator()
    if authentication_status:
        st.write("# Welcome to Pharmacy Management")
        authenticator.logout("Logout", "sidebar")
    elif not authentication_status:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

