import streamlit as st
from pages.slippage_page import show_slippage_page

def main():
    st.title('Multi-Page Streamlit App')
    st.sidebar.title('Navigation')

    # Create a selection box for page navigation
    pages = {
        'Slippage Page': show_slippage_page
        # Add more pages here if you have additional pages
    }
    page_selection = st.sidebar.selectbox('Go to', list(pages.keys()))

    # Display the selected page
    pages[page_selection]()

if __name__ == "__main__":
    main()
