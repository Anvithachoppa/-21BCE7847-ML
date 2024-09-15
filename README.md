# Langchain with Ollama Llama2

## Overview

This project is a Streamlit-based chatbot application that integrates Ollama Llama2 for language model responses. It also includes functionality for PDF document retrieval, allowing users to upload PDF files and query the content using the chatbot.

## Features

- **PDF Upload and Processing**: Upload PDF files, which are processed and split into smaller text chunks for efficient retrieval.
- **Document Storage**: The processed text chunks are stored in a vector store.
- **Query Handling**: Users can input queries, which are matched against the stored document chunks to provide relevant responses.
- **Ollama Llama2 Integration**: Uses the Ollama Llama2 model for generating responses based on the provided context and queries.

## Requirements

- Python 3.7 or later
- Streamlit
- Langchain
- Ollama Llama2
- PyMuPDF
- `python-dotenv` for environment variable management


