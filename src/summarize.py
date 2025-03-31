from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """Generates a summary of the given text."""
    summary = summarizer(text[:1024], max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']
