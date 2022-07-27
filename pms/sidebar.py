# import streamlit as st
# import time
#
# from streamlit_authenticator import Authenticate
# from streamlit_option_menu import option_menu
#
#
# def sidebar(authenticator: Authenticate):
#     with st.sidebar:
#         # https://icons.getbootstrap.com/
#         selected = option_menu("Navigational Panel",
#                                options=["Home", "Supplier", "---", 'Settings', 'Logout'],
#                                icons=['house', 'cart', None, 'gear', 'eye-slash'],
#                                menu_icon="app-indicator",
#                                default_index=0)
#
#     if selected == "Home":
#         home()
#     elif selected == "Supplier":
#         supplier()
#     elif selected == "Logout":
#         authenticator.cookie_manager.delete(authenticator.cookie_name)
#         st.session_state['logout'] = True
#         st.session_state['name'] = None
#         st.session_state['username'] = None
#         st.session_state['authentication_status'] = None
#
