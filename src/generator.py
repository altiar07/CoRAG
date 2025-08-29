from llama_cpp import Llama

class Generator:
    def __init__(self, model_path, n_ctx=2048, n_threads=6, n_batch=512):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
            n_batch=n_batch,
            n_gpu_layers=25
        )

    def generate(self, context, question, max_tokens=150):
        """
        Generate an answer to the given question using provided context.
        Uses chat-completion mode to avoid extra Q&A outputs.
        """
        output = self.llm.create_chat_completion(
            messages=[
               {
                "role": "system",
                "content": "You are a precise assistant. Answer the user's question strictly using the provided context. Output only the answer, without explanations or commentary."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
            ],
            max_tokens=max_tokens,
            stop=["Question:", "Q:"],  # prevent starting new Qs
        )

        return output["choices"][0]["message"]["content"].strip()
