# Round 1B - Persona-Driven Document Intelligence

This project processes multiple PDF documents and extracts the most relevant sections based on a given persona and job-to-be-done. It is built as part of Adobe's "Connecting the Dots" Challenge.

## 📂 Folder Structure

```
Challenge_1b/
├── Collection 1/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection 2/
│   └── ...
├── round1b_persona_pdf_analyzer.py
├── Dockerfile
├── requirements.txt
├── approach_explanation.md
└── README.md
```

## 🚀 Features

* Extracts and ranks top 5 sections relevant to a persona's task
* Subsection refinement using MiniLM embeddings
* Fast execution on CPU only
* Fully offline and Docker-compatible

## 🔧 Requirements

* Docker (recommended)
* Or Python 3.10+ and pip (for local run)

## 🐳 Run with Docker

### Step 1: Build Image

```bash
docker build --platform linux/amd64 -t round1b-analyzer:v1 .
```

### Step 2: Run Container

```bash
docker run --rm \
  -v "$(pwd)/Challenge_1b:/app/Challenge_1b" \
  --network none \
  round1b-analyzer:v1
```

## 🧪 Run Locally (Optional)

```bash
cd Challenge_1b
pip install -r requirements.txt
python round1b_persona_pdf_analyzer.py
```

## 📤 Output

Each `Collection N/` folder will contain:

```
challenge1b_output.json   ← generated result
```

## 📄 Files Explained

* `round1b_persona_pdf_analyzer.py`: Main processing script
* `requirements.txt`: Required Python packages
* `Dockerfile`: Container setup
* `approach_explanation.md`: Methodology (300–500 words)
* `README.md`: You’re reading it

## ✅ Notes

* Ensure your `PDFs/` and `challenge1b_input.json` are correctly placed inside each collection.
* Model used: `sentence-transformers/all-MiniLM-L6-v2` (offline-compatible, <100MB)

---

Built with ❤️ for Adobe India Hackathon 2025
