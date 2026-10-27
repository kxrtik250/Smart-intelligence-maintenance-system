def summarize_text(text):
    if not text: return ""
    sentences = text.strip().split('\n')
    return sentences[0][:100] if sentences else text[:100]
