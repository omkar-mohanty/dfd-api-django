import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocumentSimilarity:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def ocr_conversion(self, image_path):
        # Convert image to text using OCR
        return pytesseract.image_to_string(image_path)

    def preprocess(self, text):
        # Basic preprocessing tasks can be added here
        return text.lower()

    def vectorize(self, documents):
        return self.vectorizer.fit_transform(documents)

    def measure_similarity(self, doc_vectors):
        return cosine_similarity(doc_vectors)

    def check_threshold(self, similarity_matrix, threshold=0.8):
        # Check if similarity is above threshold
        return similarity_matrix[0][1] > threshold
