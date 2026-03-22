import streamlit as st
from rapid_jobs import fetch_rapid_jobs

st.set_page_config(layout="wide")
st.title("Real-Time Developer Job Board")

role = st.text_input("What role are you looking for?", "Software Engineer")
loc = st.text_input("Location", "Chennai")

if st.button("Search Jobs"):
    with st.spinner("Scanning LinkedIn, Indeed, and more via RapidAPI..."):
        results = fetch_rapid_jobs(query=role, location=loc)
        if results is not None and not results.empty:
            st.success(f"Found {len(results)} matches!")
            st.dataframe(results)
        else:
            st.warning("*No jobs found or API limit reached*")