import streamlit_authenticator as stauth
import fire


def hash_password(password):
    """
    Converts plain text password to hashed password
    :param password: User password to be hashed by Streamlit Authenticator
    :return: hashed password
    """
    return stauth.Hasher([password]).generate()


if __name__ == "__main__":
    fire.Fire(hash_password)