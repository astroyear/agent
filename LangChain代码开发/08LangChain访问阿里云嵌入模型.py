from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()

print(model.embed_query("你好可爱"))
print(model.embed_documents(["你好漂亮","你好帅"]))