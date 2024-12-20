import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = jsonObj, headers = headers )
    #returns an empty dict if the request was badly formatted
    if (response.status_code == 400): return get_empty_emotion_dict()
    formatted_response = json.loads(response.text)
    '''this is an example response :
    {
        "emotionPredictions": [
            {
            "emotion": {
                "anger": 0.01364663,
                "disgust": 0.0017160787,
                "fear": 0.008986978,
                "joy": 0.9719017,
                "sadness": 0.055187024
            },
            "target": "",
            "emotionMentions": [
                {
                "span": {
                    "begin": 0,
                    "end": 27,
                    "text": "I love this new technology."
                },
                "emotion": {
                    "anger": 0.01364663,
                    "disgust": 0.0017160787,
                    "fear": 0.008986978,
                    "joy": 0.9719017,
                    "sadness": 0.055187024
                }
                }
            ]
            }
        ],
        "producerId": {
            "name": "Ensemble Aggregated Emotion Workflow",
            "version": "0.0.1"
        }
    }
    
    '''
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key = lambda x: emotions[x])
    #returns the emotions with the dominant one in a dictonary format emotion : normalized_score
    return emotions

def get_empty_emotion_dict():
    return {
        "anger" :   None,
        "disgust" : None,
        "fear" :    None,
        "joy" :     None,
        "sadness" : None,
        "dominant_emotion" : None
    }