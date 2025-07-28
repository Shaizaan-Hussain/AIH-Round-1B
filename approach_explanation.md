# Round 1B - Approach Explanation

## Challenge Overview

The goal of Round 1B is to build a system that intelligently analyzes multiple PDF documents and extracts the most relevant content based on a given persona and their job-to-be-done. The output must include top sections and refined sub-sections that align closely with the task described.

## Methodology

### 1. Input Processing

Each collection folder includes:

* A `challenge1b_input.json` file defining the persona and their specific job.
* A `PDFs/` directory containing relevant documents.

The script reads the persona and job description, then formulates a semantic query by combining them into a single text prompt.

### 2. Text Extraction

We use **PyMuPDF (fitz)** to extract blocks of text from each page of every PDF. Only paragraphs longer than five words are retained to filter noise and ensure relevance. Each paragraph is stored along with its source document and page number.

### 3. Semantic Relevance Ranking

To evaluate which sections are most relevant:

* We use the **SentenceTransformer model `all-MiniLM-L6-v2`**, which converts both the query and each paragraph into embeddings.
* The **cosine similarity** score is calculated between the persona-task query and each paragraph.
* The top 5 paragraphs with the highest similarity scores are selected as the most relevant sections.

This approach ensures contextual matching beyond just keyword overlap, enabling relevance even if the wording differs.

### 4. Output Construction

The final output JSON includes:

* Metadata: persona, job, documents used, and processing timestamp.
* Extracted Sections: Document name, page number, snippet of the section, and its importance rank.
* Sub-section Analysis: Detailed view with full refined text for each section.

### 5. Constraints Handling

* The total model size is under **100MB**.
* The solution works **offline** with no internet access.
* All operations run entirely on **CPU**.
* Execution completes within **60 seconds** for typical document sets.

## Benefits

* Modular and scalable design.
* Easy integration with future NLP upgrades.
* Reliable performance across diverse document types and personas.

This architecture ensures that the system can extract high-quality insights tailored to specific user goals, making PDF reading more intelligent and task-aware.
