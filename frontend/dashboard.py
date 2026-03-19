import sys
import os
import ast

# allow Streamlit to find backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.services.paper_analysis_service import PaperAnalysisService


st.set_page_config(
    page_title="AI Research Paper Intelligence",
    layout="wide"
)

st.title("AI Research Paper Intelligence Platform")
st.write("Upload research papers and ask questions about them.")


@st.cache_resource
def load_service():
    return PaperAnalysisService()


service = load_service()


# -----------------------------
# Upload Multiple Papers
# -----------------------------

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    if st.button("Analyze Papers"):

        try:

            with st.spinner("Analyzing research papers..."):

                for uploaded_file in uploaded_files:

                    temp_path = uploaded_file.name

                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.read())

                    result = service.analyze(temp_path)

            st.success("All papers analyzed!")

            summary = result["summary"]

            st.subheader("AI Generated Research Summary")

            try:
                summary_dict = ast.literal_eval(summary)
            except:
                summary_dict = None

            if summary_dict:

                with st.expander("🧠 Problem", expanded=True):
                    st.write(summary_dict.get("Problem", ""))

                with st.expander("⚙️ Method"):
                    st.write(summary_dict.get("Method", ""))

                with st.expander("🧪 Experiments"):
                    st.write(summary_dict.get("Experiments", ""))

                with st.expander("📊 Results"):
                    st.write(summary_dict.get("Results", ""))

                with st.expander("✅ Conclusion"):
                    st.write(summary_dict.get("Conclusion", ""))

            else:
                st.write(summary)

        except Exception as e:
            st.error(f"Error occurred: {str(e)}")


# -----------------------------
# RAG CHATBOT SECTION
# -----------------------------

st.markdown("---")
st.info(
"Tip: Ask questions like 'What dataset was used?', "
"'What problem does the paper address?', "
"or 'What results were achieved?'"
)
st.subheader("💬 Ask Questions About the Papers")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask a question about the uploaded papers")

if query:

    with st.spinner("Searching papers..."):

        answer = service.answer_question(query)

    st.session_state.chat_history.append((query, answer))


# display conversation
for q, a in st.session_state.chat_history:

    st.markdown("### 🧑 Question")
    st.write(q)

    st.markdown("### 🤖 Answer")
    st.write(a)

    st.divider()