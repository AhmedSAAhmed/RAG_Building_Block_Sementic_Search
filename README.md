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

## System-Level Explanation of the RAG Workflow

Retrieval-Augmented Generation (RAG) relies on a critical two-stage pipeline: **retrieval followed by generation**. 

First, the **retriever** searches the database to select the top-k most relevant documents based on the user's query. Next, these selected documents are injected into the prompt and passed to a Large Language Model (the **generator**). The generator uses this retrieved context to synthesize a factual, grounded answer. This architecture is what powers leading real-world systems like **Perplexity**, **GitHub Copilot**, and **ChatGPT**, allowing them to answer questions based on external, up-to-date knowledge rather than just their training weights.

### Tying Retrieval Metrics to Generation Quality
The quality of the final generated answer is entirely dependent on the retriever's accuracy. If the retriever fails to fetch the right documents, the generator will produce a poor or hallucinated answer. 

Looking at our performance table, we can see exactly why the evolution from keyword search to semantic search is critical for downstream RAG quality:
* **BM25 (Keyword Search):** With a Recall@5 of **0.7266**, it performs decently but relies on exact lexical matches. If the user query uses synonyms, BM25 might fail to retrieve the necessary context, leaving the LLM to guess.
* **Word2Vec (Early Semantic):** At a Recall@5 of **0.5032**, it struggles with complex phrases and out-of-vocabulary words, providing the weakest context for the generator.
* **Transformers (Semantic Search):** Achieves the highest Recall@5 of **0.9298** by capturing true contextual meaning in dense vector spaces. 

Because the Transformer improves Recall@5 by over 20% compared to BM25, it guarantees that the generator receives the correct context in the top 5 results ~93% of the time. Better retrieval means better context, which directly translates to a vastly superior and more reliable generated answer.
