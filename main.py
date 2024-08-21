import streamlit as st
import hashlib

# Dummy user database (replace with a real database)
users = {
    "username": hashlib.sha256("password".encode()).hexdigest()
}

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login function
def login(username, password):
    if username in users and users[username] == hash_password(password):
        return True
    return False

# Streamlit app
def main():
    st.title("Secure Text Storage")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.header("Please Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your username and password.")
    else:
        st.header("Secure Text")
        text_area = st.text_area("Your secure text", height=200)
        if st.button("Save"):
            st.success("Text saved successfully!")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.warning("Logged out successfully.")

if __name__ == '__main__':
    main()
