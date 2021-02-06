import json

import requests
import streamlit as st


def main():
    # Some Basic Configuration for StreamLit
    st.beta_set_page_config(
        page_title="Title of the webpage",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    # Just making sure we are not bothered by File Encoding warnings
    st.set_option("deprecation.showfileUploaderEncoding", False)
    # List of Available Web Pages to be rendered by the app
    pages = ["Home", "UserInfo", "RepoInfo", "Pull Requests"]
    p_choice = st.sidebar.selectbox("Menu", pages)
    if p_choice == "Home":
        st.title("Welcome to GitKundli")


if __name__ == "__main__":
    main()
