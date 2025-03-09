---
title: Resume AI Chatbot
emoji: 🤖
colorFrom: blue
colorTo: yellow
sdk: gradio
sdk_version: 5.20.0
app_file: app.py
pinned: false
---

# Resume Chatbot

An AI powered virtual assistant that answers questions about my professional background using my resume database.

## Motivation

I want my resume site to be clean and sleek. However, I also want to allow visitors to gain more information about my projects, work history, etc. My solution is a chatbot powered by Retrieval-Augmented Generation (RAG). This way I can add as much information as desired about my work, and potential employers can ask the chatbot directly. The system works by searching through my detailed resume database to find relevant information, then using OpenAI's language model to generate natural, conversational responses.

## Tech Stack

The Resume Chatbot is built using a modern AI stack:

- LangChain: For orchestrating the retrieval and generation pipeline
- Chroma: Vector database for efficient semantic search across resume content
- OpenAI: Powering the natural language understanding and response generation

## How It Works

1. User Query: Visitor asks a question about my professional experience
2. Query Processing: The system processes the query while maintaining the full conversation history for context
3. Retrieval: Chroma searches the resume database for the most relevant information
4. Context Assembly: Retrieved resume sections are compiled into a comprehensive prompt
5. Response Generation: OpenAI transforms the prompt and retrieved context into a natural, conversational response

Note: This entire workflow is orchestrated through a LangChain sequential chain, where each step passes its output to the next component in the pipeline. The chain handles memory management, retrieval augmentation, and prompt construction following industry-standard RAG best practices.
