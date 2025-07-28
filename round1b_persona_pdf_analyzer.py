import os
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
import fitz  # PyMuPDF

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_paragraphs(pdf_path):
    paragraphs = []
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if len(text.split()) > 5:
                paragraphs.append({
                    "text": text,
                    "page": page_num,
                    "doc": os.path.basename(pdf_path)
                })
    return paragraphs

def rank_paragraphs(paragraphs, persona_query):
    query_embedding = model.encode(persona_query, convert_to_tensor=True)
    for para in paragraphs:
        para_embedding = model.encode(para["text"], convert_to_tensor=True)
        score = util.cos_sim(query_embedding, para_embedding).item()
        para["score"] = score
    ranked = sorted(paragraphs, key=lambda x: x["score"], reverse=True)
    return ranked[:5]  # top 5 sections

def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_dir = os.path.join(collection_path, "PDFs")

    with open(input_path, 'r') as f:
        input_data = json.load(f)

    persona = input_data["persona"]
    job = input_data["job"]
    query = persona + ": " + job

    all_paragraphs = []
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            all_paragraphs.extend(extract_paragraphs(os.path.join(pdf_dir, pdf_file)))

    top_sections = rank_paragraphs(all_paragraphs, query)

    output = {
        "metadata": {
            "persona": persona,
            "job": job,
            "timestamp": datetime.now().isoformat(),
            "documents": os.listdir(pdf_dir)
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for idx, para in enumerate(top_sections, start=1):
        output["extracted_sections"].append({
            "document": para["doc"],
            "page_number": para["page"],
            "section_title": para["text"][:50] + ("..." if len(para["text"]) > 50 else ""),
            "importance_rank": idx
        })
        output["subsection_analysis"].append({
            "document": para["doc"],
            "page_number": para["page"],
            "refined_text": para["text"]
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

def process_all_collections(base_dir="Challenge_1b"):
    for folder in os.listdir(base_dir):
        collection_path = os.path.join(base_dir, folder)
        if os.path.isdir(collection_path):
            print(f"Processing {folder}...")
            process_collection(collection_path)

if __name__ == "__main__":
    process_all_collections()

