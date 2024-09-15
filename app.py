#LANGCHAIN_API_KEY="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"

#LANGCHAIN_PROJECT="chatbot project"



from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.vectorstores import SimpleVectorStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM (Ollama Llama2)
llm = Ollama(model="llama2")

# Create the chatbot prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide responses to user queries based on the provided documents."),
        ("user", "Question: {question}\n\nContext: {context}")
    ]
)

# Streamlit framework for the app
st.title("ChatBot Trademarkia")
input_text = st.text_input("Search the topic you want")

# Initialize the document store
doc_store = SimpleVectorStore()

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Load and process PDF
    loader = PyMuPDFLoader(uploaded_file)
    documents = loader.load()
    
    # Split documents into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    
    # Add chunks to the document store
    for chunk in chunks:
        doc_store.add_document(chunk)

if input_text:
    # Query the document store
    query_results = doc_store.search(input_text)

    if query_results:
        # Format the prompt with the user's input and query results
        context = " ".join(query_results)
        formatted_prompt = prompt.format(question=input_text, context=context)

        # Get the LLM response
        response = llm(formatted_prompt)

        # Output the response in the Streamlit app
        st.write(response)
    else:
        st.write("No relevant information found.")
