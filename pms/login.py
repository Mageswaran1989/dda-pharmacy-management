import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml import SafeLoader

# Initialize connection.
# Uses st.experimental_singleton to only run once.
# @st.experimental_singleton
def init_authenticator():
    with open('config/root_credentials.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')

    print(name, authentication_status, username)
    return authenticator, name, authentication_status, username