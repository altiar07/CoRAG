from src.retriever import Retriever
from src.generator import Generator
from src.utils import load_documents_from_data

MODEL_PATH = "models/phi-3-mini-4k-instruct.Q4_K_M.gguf"

# ===== Load Documents (auto handles txt + pdf) =====
docs = load_documents_from_data("data")

retriever = Retriever()
retriever.add_documents(docs)

generator = Generator(MODEL_PATH)

print("💬 RAG Chat Mode (type 'exit' to quit)\n")
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    retrieved_docs = retriever.retrieve(question)
    context = "\n".join(retrieved_docs)

    answer = generator.generate(context, question)
    print(f"AI: {answer}\n")
