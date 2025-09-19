from langchain.vectorstores import Chroma
from langchain.document_loaders.json_loader import JSONLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from ..provider import LLMProvider


class VectorStore:
    """A class to handle vector storage and querying using LangChain and Chroma."""

    def __init__(self, json_file: str, llm: LLMProvider):
        """Initialize the VectorStore with a CSV file and an LLM instance."""
        self.llm = llm
        self.api_key = llm.configs.get('api_key')
        self.base_url = llm.configs.get('base_url')
        self.db = self.load_data(json_file)

    def load_data(self, json_file):
        """Load data from a CSV file and create a Chroma vector store."""
        loader = JSONLoader(file_path=json_file, jq_schema=".[]", text_content=False)
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        split_docs = splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings(base_url=self.base_url, api_key=self.api_key)
        db = Chroma.from_documents(split_docs, embeddings)
        return db

    def query(self, query_text, top_k=5):
        """Query the vector store for similar documents."""
        similar_docs = self.db.similarity_search(query_text, k=top_k)
        return similar_docs
