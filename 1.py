# ...existing code...
import tiktoken

# Try model-based encoding first, fall back to a known encoding name
try:
    enc = tiktoken.encoding_for_model("gpt-4o")
except Exception:
    enc = tiktoken.get_encoding("cl100k_base") #gpt-4 token

tokens = enc.encode("ChatGPT is amazing!")
print(tokens)
print(len(tokens))

# decode expects an iterable of token ids; pass a list
print(enc.decode([14065]))
# ...existing code...