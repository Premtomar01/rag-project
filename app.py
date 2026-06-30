import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Hybrid RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Hybrid RAG Assistant")
st.write("Ask questions about Company Policies or Employee Database.")

query = st.text_input("Ask Question")

if st.button("Ask"):

    if query.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={
                    "question": query
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Answer")

                st.write(data["answer"])

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.info(f"Route : {data['route']}")

                with col2:

                    st.info(f"Confidence : {data['confidence']}")

                st.subheader("Sources")

                for source in data["sources"]:

                    st.write("✅", source)

            else:

                st.error("Unable to connect to FastAPI backend.")