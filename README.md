# RAG Workflow

## How Retrieval Supports a RAG Pipeline

Retrieval-Augmented Generation (RAG) combines a **retriever** with a
**generator** to produce more accurate and grounded responses.

The workflow consists of two main stages:

1.  **Retrieval**
    -   The retriever searches a document collection and identifies the
        most relevant documents for the user's query.
    -   Different retrieval methods can be used, including keyword
        search (BM25), TF-IDF vector search, and transformer-based
        semantic search.
2.  **Generation**
    -   The retrieved documents are provided as context to a Large
        Language Model (LLM), which generates the final answer.
    -   Instead of relying only on its pre-trained knowledge, the model
        grounds its response using the retrieved information, reducing
        hallucinations and improving factual accuracy.

This retrieval-first, generation-second architecture is the foundation
of modern RAG systems.

## Real-World Example

A well-known example is **ChatGPT** when it uses retrieval over uploaded
files or connected knowledge sources. Before generating an answer, the
system retrieves the most relevant passages from the available documents
and then uses those passages as context for the language model.

Other production systems such as **Microsoft Copilot** and **Perplexity
AI** also follow this Retrieval-Augmented Generation approach, where
retrieval occurs before generation to improve answer quality and provide
responses grounded in external knowledge.

## Evolution of Retrieval Methods

Information retrieval has evolved from traditional lexical matching to
semantic understanding.

-   **BM25** ranks documents using keyword frequency and term
    importance. It performs well when queries closely match the document
    vocabulary but struggles with synonyms and paraphrased text.
-   **TF-IDF** represents documents as weighted vectors, improving
    document ranking while still relying primarily on lexical
    similarity.
-   **Transformer-based semantic search** generates dense embeddings
    that capture the meaning of text, allowing relevant documents to be
    retrieved even when different words are used.

This progression demonstrates how retrieval systems have moved from
exact keyword matching toward understanding the semantic meaning of
queries and documents.

## Why Retrieval Quality Matters

The quality of the retrieved documents directly affects the quality of
the generated answer. If the retriever returns irrelevant or incomplete
context, even a powerful language model may produce inaccurate or
hallucinated responses.

The evaluation results from this project demonstrate this relationship:

  Retrieval Method                Mean Reciprocal Rank (MRR)
  ----------------------------- ----------------------------
  BM25                                                0.6738
  TF-IDF                                              0.9044
  Transformer Semantic Search                         0.9044

The transformer-based retriever achieved the highest MRR, indicating
that it retrieves more relevant documents than the lexical approaches.
In a RAG pipeline, this higher retrieval quality provides the language
model with better context, leading to more accurate and reliable
generated answers.
