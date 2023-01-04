import re
import string


def preprocess_text(text):
    # Remove links
    text = re.sub(r"http\S+", "", text)
    
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)
    
    text = text.strip().lower()
    text = re.sub(
        f"[{re.escape(string.punctuation)}]", "", text
    )
    return text