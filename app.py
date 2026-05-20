from groq import Groq

client = Groq(api_key="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")

try:
    with open("document.txt", "r") as f:
        document = f.read()

    print("Document AI Ready!")
    question = input("Ask a question about your document: ")
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"Answer questions based on this document:\n\n{document}"},
            {"role": "user", "content": question}
        ]
    )
    print(f"\nAnswer: {response.choices[0].message.content}")

except Exception as e:
    print(f"Error: {e}")
