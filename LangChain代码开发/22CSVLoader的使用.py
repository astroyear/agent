from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter":",",  #指定分割符
        "quotechar":'"',  #当一个值带逗号的时候，用""括起来代表一个整体，这里指明""内的逗号是里面的
        "fieldnames":['a','b','c','d'] #指定表头，会把原来的表头当数据用，仅在无表头的情况下使用
    },
    encoding="utf-8"
)

# #批量加载
# documents = loader.load()
# for document in documents:
#     print(type(document),document)

#懒加载
for document in loader.lazy_load():
    print(document)