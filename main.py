from rag_chain import qa

if __name__ == "__main__":
    query = input("Ask something: ")
    result = qa.invoke(query)
    print("\nAnswer:", result)
