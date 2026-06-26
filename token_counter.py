import tiktoken
enc=tiktoken.encoding_for_model("gpt-4o")
tokens=enc.encode("ChatGPT is amazing!")
print(tokens)
print(len(tokens))
print(enc.decode([14065]))