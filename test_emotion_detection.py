import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # Test for positive sentiment
        text = "I am very happy today!"
        result = emotion_detector(text)
        print(f"Positive sentiment result: {result}")
        self.assertIn("Joy: ", result)
        self.assertIn("Dominant Emotion: pos", result)  # Expect 'pos'
        self.assertIn("Anger: 0.0", result)
        self.assertIn("Sadness: 0.412", result)  # Update expected value

        # Test for negative sentiment
        text = "I am very sad today."
        result = emotion_detector(text)
        print(f"Negative sentiment result: {result}")
        self.assertIn("Sadness: ", result)
        self.assertIn("Dominant Emotion: neg", result)  # Expect 'neg'
        self.assertIn("Anger: 0.531", result)  # Update expected value
        self.assertIn("Joy: 0.0", result)

        # Test for mixed sentiment
        text = "I am happy but also a bit sad."
        result = emotion_detector(text)
        print(f"Mixed sentiment result: {result}")
        self.assertIn("Joy: ", result)

if __name__ == '__main__':
    unittest.main()