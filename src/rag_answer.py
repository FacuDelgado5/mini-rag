import ollama

# generate an answer using the retrieved context
def answer_with_context(query, context):
    prompt = f"""
You are a helpful assistant answering questions about a document.

Use only the information from the context below.
If the answer is not in the context, say:
"No encontré la respuesta en el documento."

Answer in Spanish and keep the answer clear and concise.

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": 200
        }
    )

    return response["message"]["content"]