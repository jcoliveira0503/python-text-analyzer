from collections import Counter
import re

def analyze(text):
    words = re.findall(r"\b[\wÀ-ÿ]+\b", text.lower())
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    counts = Counter(words)

    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "average_words_per_sentence": round(len(words) / len(sentences), 2) if sentences else 0,
        "most_common_words": counts.most_common(5),
    }

if __name__ == "__main__":
    sample = input("Enter a text: ")
    result = analyze(sample)
    print("\nText Analysis")
    print("Characters:", result["characters"])
    print("Words:", result["words"])
    print("Sentences:", result["sentences"])
    print("Average words per sentence:", result["average_words_per_sentence"])
    print("Most common words:", result["most_common_words"])
