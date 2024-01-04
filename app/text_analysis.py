from textblob import TextBlob



def get_sentiment_score(sentence):
    analysis = TextBlob(sentence)
    return analysis.sentiment.polarity

def calculate_mean(numbers):
    if not numbers:
        return None  # Handle empty list to avoid division by zero

    total = sum(numbers)
    mean = total / len(numbers)
    return mean