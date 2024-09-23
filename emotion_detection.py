from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon, this should be done once.
nltk.download('vader_lexicon')

def emotion_detector(text_to_analyze):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text_to_analyze)
    
    anger = scores['neg']
    joy = scores['pos']
    sadness = scores['neu']
    disgust = 0
    fear = 0
    
    # Determine the dominant emotion based on pos, neg, and neu scores
    dominant_emotion = max(('pos', joy), ('neg', anger), ('neu', sadness), key=lambda x: x[1])[0]
    
    result = (
        f"Anger: {anger}\n"
        f"Joy: {joy}\n"
        f"Sadness: {sadness}\n"
        f"Disgust: {disgust}\n"
        f"Fear: {fear}\n"
        f"Dominant Emotion: {dominant_emotion}"
    )
    
    return result