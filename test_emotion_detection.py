from EmotionDetection.emotion_detection import emotion_detector
import unittest

if __name__ == "__main__" : 
    test = "I love this new technology."
    print(emotion_detector(test))