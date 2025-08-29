from src.retriever import Retriever
from src.generator import Generator
from src.utils import load_text_file
import glob

# ===== Config =====
MODEL_PATH = "models/Phi-3-mini-4k-instruct-q4.gguf"

# ===== Load Documents =====
docs = []
for file_path in glob.glob("data/*.txt"):
    docs.extend(load_text_file(file_path))

# ===== Init Retriever & Index Documents =====
retriever = Retriever()
retriever.add_documents(docs)

# ===== Load LLM Once =====
generator = Generator(MODEL_PATH)

# ===== Interactive Loop =====
print("💬 RAG Chat Mode (type 'exit' to quit)\n")
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Retrieve relevant context
    retrieved_docs = retriever.retrieve(question)
    context = "\n".join(retrieved_docs)

    # Generate answer
    answer = generator.generate(context, question)

    # Display result
    print(f"AI: {answer}\n")
