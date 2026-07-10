# RAG Building Block: Semantic Search 🔍

This repository demonstrates a fundamental building block for Retrieval-Augmented Generation (RAG) systems, focusing on semantic search capabilities. It allows for a comparative analysis of different retrieval methods—BM25 (keyword-based), Word2Vec (static embeddings), and Transformer-based (semantic embeddings)—to understand their impact on RAG performance.

## 🌟 Features

*   **Multi-Retriever Comparison:** Directly compare the effectiveness of BM25, Word2Vec, and Transformer-based retrieval methods.
*   **RAG Answer Generation:** Optionally enable RAG answers using an OpenAI API key, showcasing how retrieval quality affects generated responses.
*   **Interactive Streamlit Demo:** A user-friendly web application built with Streamlit to visualize retrieval results and RAG answers.
*   **Performance Metrics:** Evaluates retrieval performance using standard Information Retrieval metrics like Precision, Recall, and MRR.
*   **Customizable Retrieval:** Easily adjust the number of documents retrieved for comparison.
*   **Demo Corpus:** Utilizes a curated corpus of documents about a fictional company, "TechFlow AI," for realistic demonstration.

## 🚀 Tech Stack

*   **Languages:** Python
*   **Frameworks:** Streamlit, Sentence-Transformers, Hugging Face Transformers, PyTorch, Gensim, Scikit-learn
*   **Libraries:** Pandas, NumPy, Matplotlib, Tqdm, OpenAI API

## 🔧 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AhmedSAAhmed/RAG_Building_Block_Sementic_Search.git
    cd RAG_Building_Block_Sementic_Search
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up OpenAI API Key (for RAG answers):**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## ▶️ Usage

This project provides a Streamlit application to explore the retrieval methods.

1.  **Run the Streamlit application:**
    Navigate to the project's root directory and run:
    ```bash
    streamlit run streamlit/app.py
    ```

2.  **Interact with the Demo:**
    *   The application will open in your browser.
    *   **Sidebar Configuration:**
        *   **Enable RAG Answers:** Check this box to generate answers using retrieved documents (requires OpenAI API key).
        *   **Number of documents to retrieve:** Adjust the slider to set how many documents each retriever should fetch (default is 3).
        *   **Show debug info:** Enable to see detailed ranking information.
    *   **Corpus View:** Expand the "View Demo Corpus" section to see the sample documents about TechFlow AI.
    *   **Query Input:** Use the provided sample queries or enter your own.
    *   **Results:** Observe the retrieved documents for each method and, if RAG is enabled, the generated answers.

## 💡 How to Use

This project serves as a practical demonstration of how different retrieval strategies impact the quality of information fed into a RAG system. By comparing BM25, Word2Vec, and Transformer-based retrievers on the same queries, users can gain insights into:

*   **Keyword vs. Semantic Matching:** Understanding the difference between exact keyword matches (BM25) and nuanced semantic similarity (Word2Vec, Transformers).
*   **Embedding Effectiveness:** Appreciating how sophisticated embeddings (like those from `all-mpnet-base-v2`) can better capture context and meaning, leading to more relevant document retrieval.
*   **RAG Pipeline Components:** Recognizing retrieval as a critical first step in any RAG pipeline, directly influencing the LLM's ability to generate accurate and contextually appropriate answers.

This tool is valuable for developers and researchers working on RAG systems, information retrieval, or natural language understanding, allowing them to experiment with and select the most suitable retrieval mechanisms for their specific use cases.

## 📁 Project Structure

```
RAG_Building_Block_Sementic_Search/
├── notebooks/
│   └── unified_retrieval_comparison.ipynb
├── streamlit/
│   ├── app.py
│   ├── demo_data.py
│   └── rag_system.py
├── src/
│   ├── __init__.py
│   ├── bm25_retriever.py
│   ├── data.py
│   ├── data_loader.py
│   ├── embedding_generator.py
│   ├── evaluator.py
│   ├── helpers.py
│   ├── model.py
│   ├── optimization.py
│   ├── predictor.py
│   ├── retriever.py
│   ├── train.py
│   ├── transfer.py
│   ├── transformer_retriever.py
│   ├── utils.py
│   └── word2vec_retriever.py
├── tests/
│   ├── bm25_retriever_20251115_111906.json
│   ├── evaluator_20251115_111906.json
│   ├── test
│   ├── test_bm25_retriever.py
│   ├── test_evaluator.py
│   ├── test_transformer_retriever.py
│   ├── test_word2vec_retriever.py
│   ├── transformer_retriever_20251115_111909.json
│   └── word2vec_retriever_20251115_111909.json
├── .env.example
├── requirements.txt
└── README.md
```

## 📚 Dependencies

*   **Core Libraries:** `torch`, `transformers`, `sentence-transformers`, `datasets`, `faiss-cpu`, `scikit-learn`, `rank-bm25`, `beir`, `gensim`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `jupyter`, `tqdm`
*   **Demo App:** `streamlit`, `openai`, `python-dotenv`

## 🧪 Testing

Unit tests are available in the `tests/` directory. You can run them using `unittest`:

```bash
python -m unittest discover tests
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## 📄 License

No license information was provided for this repository.

## 🔗 Important Links

*   **Repository:** [RAG_Building_Block_Sementic_Search](https://github.com/AhmedSAAhmed/RAG_Building_Block_Sementic_Search)

## footer

---

© 2024 [AhmedSAAhmed](https://github.com/AhmedSAAhmed) | [Project Repository](https://github.com/AhmedSAAhmed/RAG_Building_Block_Sementic_Search)

Feel free to **fork**, **star ⭐**, and **watch** the repository for updates!


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**
