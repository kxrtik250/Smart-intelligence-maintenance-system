from PyPDF2 import PdfReader
def extract_text_from_pdf(path):
    try:
        reader = PdfReader(path)
        texts = [p.extract_text() or '' for p in reader.pages]
        return '\n'.join(texts)
    except Exception:
        return ''
