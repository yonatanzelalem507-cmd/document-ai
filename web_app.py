import streamlit as st
from groq import Groq

st.set_page_config(page_title="Global Care Medical Center", page_icon="🏥", layout="wide")

st.markdown("""
<style>
.main { background-color: #003580; }
.stApp { background-color: #003580; color: white; }
h1 { color: white; font-size: 50px; }
p { color: white; }
.stTextInput input { background-color: white; }
.stButton button { background-color: #f0a500; color: white; font-size: 18px; padding: 10px 30px; border-radius: 5px; border: none; }
</style>
""", unsafe_allow_html=True)

client = Groq(api_key=st.secrets"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")

st.title("🏥 Global Care Medical Center")
st.subheader("A Promise of Hope Through World Class Healthcare")
st.write("---")

with open("document.txt", "r") as f:
    document = f.read()

question = st.text_input("Ask our AI Assistant anything about our hospital:")

if st.button("Send Enquiry"):
    if question:
        with st.spinner("Getting your answer..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": f"Answer based on this document:\n\n{document}"},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)



