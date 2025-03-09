import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def initialize_database(db_name):
    # Get all files in knowledge base
    documents = []
    loader = DirectoryLoader(
        "knowledge-base",
        glob="**/*.md",
        loader_cls=TextLoader,
    )
    docs = loader.load()
    for doc in docs:
        documents.append(doc)

    # Split data into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Create OpenAIEmbeddings model to convert text into numerical vector representations
    embeddings = OpenAIEmbeddings()

    # Delete db if already exists. Otherwise we will append
    # to existing db
    if os.path.exists(db_name):
        Chroma(
            persist_directory=db_name, embedding_function=embeddings
        ).delete_collection()

    # Create db, embed text (convert text to vectors) and populate vector database with embeddings
    return Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=db_name
    )
