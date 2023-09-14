import os
from utils.template_matching import store_template, match_template
from utils.pdf_tools import convert_pdf_to_image
from document.document  import DocumentSimilarity

# Directory paths
TEMPLATES_DIR = "data/templates"

# Ensure directories exist
# TFID
os.makedirs(TEMPLATES_DIR, exist_ok=True)

def main():
    # image_paths = convert_pdf_to_image(pdf_path="./data/raw_documents/10089969_2020_010.pdf", output_folder="./data/processed_images")
    # image_path = image_paths[0]
    # store_template(image_path, TEMPLATES_DIR)
    
    # image_paths = convert_pdf_to_image(pdf_path="./data/raw_documents/sem1_fake.pdf", output_folder="./data/processed_images")
    # image_path = image_paths[0]
    # match_template(image_path, TEMPLATES_DIR)

    doc_sim = DocumentSimilarity()
    doc1 = './data/processed_images/sem1.png'
    doc2 = './data/processed_images/sem2.png'
    
    doc1_text = doc_sim.ocr_conversion(doc1)
    doc2_text = doc_sim.ocr_conversion(doc2)

    documents = [doc_sim.preprocess(doc1_text), doc_sim.preprocess(doc2_text)]
    doc_vectors = doc_sim.vectorize(documents)
    print(doc_vectors)
    similarity_matrix = doc_sim.measure_similarity(doc_vectors)

    print(similarity_matrix[0][1])
    if doc_sim.check_threshold(similarity_matrix, 0.7):
        print("Documents are similar!")
    else:
        print("Documents are not similar!")


if __name__ == "__main__":
    main()
