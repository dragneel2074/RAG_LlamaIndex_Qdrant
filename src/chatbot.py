from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.core import PromptTemplate

def create_chat_engine(index, llm):
    memory = ChatMemoryBuffer.from_defaults(token_limit=4500)
    
    template = (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question and each answer should end with Thank You for asking: {query_str}\n"
    )
    qa_template = PromptTemplate(template)
    
    chat_engine = CondensePlusContextChatEngine.from_defaults(
        index.as_retriever(),
        memory=memory,
        llm=llm,
        text_qa_template=qa_template
    )
    
    return chat_engine