from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def create_conversation_chain(MODEL, vectorstore):
    # create a new Chat with OpenAI
    llm = ChatOpenAI(temperature=0.7, model_name=MODEL)

    # set up the conversation memory for the chat
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # the retriever is an abstraction over the VectorStore that will be used during RAG.
    # we may need to increse the k value (number of chunks to send) as knowledge base grows
    retriever = vectorstore.as_retriever(search_kwargs={"k": 12})

    # set up the conversation chain with the LLM, vector store and memory
    return ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory
    )
