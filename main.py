import streamlit as st
from pages.slippage_page import show_slippage_page

def main():
    st.title('Multi-Page Streamlit App')
    st.sidebar.title('Navigation')

    # Create a selection box for page navigation
    pages = {
        'Slippage Page': 'Slippage Page',
        'Page 2': 'Page 2',  # Placeholder for additional pages
        'Page 3': 'Page 3',  # Placeholder for additional pages
        # Add more pages here if you have additional pages
    }
    page_selection = st.sidebar.selectbox('Go to', list(pages.keys()))

    # Display the selected page
    if page_selection == 'Slippage Page':
        show_slippage_page()
    elif page_selection == 'Page 2':
        st.write("This is Page 2. Add your content here.")
    elif page_selection == 'Page 3':
        st.write("This is Page 3. Add your content here.")
    # Add more conditions for additional pages here

if __name__ == "__main__":
    main()
