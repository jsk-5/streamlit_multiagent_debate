import streamlit as st
import boto3

from botocore.client import Config
from langchain.chains import RetrievalQA
from langchain_aws import BedrockLLM
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
import time


def response_generator(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="O9O2CCKXV4",
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
)

model_kwargs_claude = {"temperature": 0, "top_k": 10, "max_tokens_to_sample": 3000}

llm = BedrockLLM(model_id="anthropic.claude-v2", model_kwargs=model_kwargs_claude)

qa = RetrievalQA.from_chain_type(
    llm=llm, retriever=retriever, return_source_documents=True
)


st.title("Rag test")

# Set OpenAI API key from Streamlit secrets

# Set a default model
if "anthropic_model" not in st.session_state:
    st.session_state["anthropic_model"] = "anthropic.claude-v2"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me a question about my data"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = qa(prompt)['result']
        st.write_stream(response_generator(response))
        # st.markdown(response)
        # print(response)
    st.session_state.messages.append({"role": "assistant", "content": response})