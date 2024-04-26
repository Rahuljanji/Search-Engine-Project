import streamlit as st 
import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.get_collection(name="ENGINE")

st.set_page_config(page_title="SubHunt", page_icon="🎬", layout="wide")
st.title("Welcome to SubHunt 🍿")

st.sidebar.title("Search")
title = st.sidebar.text_input("Enter your search")
if st.sidebar.button("Search"):
    title = [title]
    results = collection.query(
        query_texts=title,
        n_results=10
    )
    if results['metadatas']:
        st.subheader("Search Results")
        for result in results['metadatas']:
            st.write(result)
    else:
        st.warning("No results found.")

# About section
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple web application for searching movie subtitles. "
    "It uses ChromaDB for efficient searching. Enjoy!"
)

# Main content
st.write("""
## What is SubHunt?
SubHunt is a web application that allows you to easily search for subtitles of your favorite movies.
""")

st.write("""
### How to use?
1. Enter the title of the movie you want to search for in the sidebar.
2. Click on the 'Search' button.
3. The search results will be displayed below.
""")

st.write("""
### Technologies Used:
- [Streamlit](https://streamlit.io/) for building the web application.
- [ChromaDB](https://chromadb.org/) for efficient searching of movie subtitles.
""")

st.write("""
### About the Developer:
This web application is developed by [Your Name]. If you have any questions or suggestions, feel free to reach out!
""")
