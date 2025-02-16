import streamlit as st
from openai import OpenAI as OpenAIClient

base_url = "https://api.aimlapi.com/v1"
api_key = "64728cd6830144558598b8886f53f787"
system_prompt = "You are a song writer and always answer using rhymes and poetic devices"

api = OpenAIClient(api_key=api_key, base_url=base_url)

def get_response(user_prompt):
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )
    return completion.choices[0].message.content

st.title("AI Songwriter")
user_prompt = st.text_area("Enter your prompt:")

if st.button("Generate Lyrics"):
    if user_prompt:
        response = get_response(user_prompt)
        st.text_area("AI Response:", response, height=200)
        with open("response.txt", "w", encoding="utf-8") as file:
            file.write(f"User: \n {user_prompt}\n")
            file.write(f"AI: \n {response}\n")
        st.success("Response saved to response.txt")

