from llama_index.llms.gemini import Gemini
from document_processor import load_documents_from_web, load_documents_from_directory
from indexer import create_index
from chatbot import create_chat_engine

def main():
    # Initialize LLM
    llm = Gemini()
    
    # Load documents (you can switch between web and directory loading)
    # documents = load_documents_from_web(["https://www.example.com"])
    documents = load_documents_from_directory()
    
    # Create index
    index = create_index(documents, llm)
    
    # Create chat engine
    chat_engine = create_chat_engine(index, llm)
    
    print("Chatbot is ready. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = chat_engine.chat(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()