import streamlit as st
import os
from src.process_pdf import extract_text_from_pdf
from src.summarize import summarize_text
from src.fetch_papers import fetch_arxiv_papers

# Ensure 'uploads/' directory exists
uploads_dir = "uploads"
os.makedirs(uploads_dir, exist_ok=True)

st.title("📚 AI-Powered Research Assistant")

# User selection - Choose either Upload or Keyword Search
option = st.radio("Select an Option:", ["🔄 Upload Research Paper", "🔎 Search by Keyword"])

# Upload Research Paper (Only Visible if Option is Selected)
if option == "🔄 Upload Research Paper":
    uploaded_file = st.file_uploader("📜 Upload a Research Paper (PDF)", type=["pdf"])
    
    if uploaded_file:
        st.subheader("📜 Processing & Summarizing Paper...")

        # Save PDF
        pdf_path = os.path.join(uploads_dir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract Full Text
        extracted_text = extract_text_from_pdf(pdf_path)
        if not extracted_text:
            st.error("❌ Unable to extract text from PDF. Please try another file.")
        else:
            # Generate a longer summary
            summary = summarize_text(extracted_text[:10000])  # Increased text limit for better summaries

            if summary:
                st.subheader("📄 Detailed Summary")
                st.write(summary)
            else:
                st.error("❌ Summarization failed.")

            # Fetch ONLY related papers based on content of the uploaded file
            st.subheader("📚 Relevant Research Papers")
            related_papers = fetch_arxiv_papers(uploaded_file.name.split(".")[0])  # Using file name as query
            if related_papers:
                for paper in related_papers:
                    st.markdown(f"- [{paper['title']}]({paper['url']})")
            else:
                st.warning("⚠ No highly relevant papers found.")

# Search by Keyword (Only Visible if Option is Selected)
elif option == "🔎 Search by Keyword":
    query = st.text_input("Enter Research Keyword or Topic")

    if query:
        st.subheader("🔍 Highly Relevant Papers from ArXiv")
        papers = fetch_arxiv_papers(query)
        if papers:
            for paper in papers:
                st.markdown(f"- [{paper['title']}]({paper['url']})")
        else:
            st.warning("⚠ No highly relevant papers found.")
