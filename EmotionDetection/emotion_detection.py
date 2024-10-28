import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = {"raw_document": {"text": text_to_analyze}}

    # Send POST request to the EmotionPredict endpoint
    response = requests.post(URL, headers=Headers, json=Input_json)
    
    # Check if the request was successful
    if response.status_code == 200:
        #Add JSON response to debug when script failed to work
        response_json = json.loads(response.text) #added json.loads to convert to dictionary
        #print("Response JSON:", response_json)

        #Added this because of the response JSON I recieved after repeated errors
        emotions = response_json['emotionPredictions'][0]['emotion']

        #Script for dominate emotion
        dominant_emotion = max(emotions, key=emotions.get)

        #Prescribed dictionary format
        #This didnt work. I recieved a NameError because the "xxx_score" part is not defined for each line.
        #emotion_dictionary = {
            #'anger': anger_score,
            #'disgust': disgust_score,
            #'fear': fear_score,
            #'joy': joy_score,
            #'sadness': sadness_score,
            #'dominant_emotion': '<name of the dominant emotion>'}

        #Here is an attempt to fix the above issue:
        emotion_dictionary = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

        #This was original but failed
        #return response.json()['text']  # Return the text attribute of the response object

        #After i discovered the emotionPredictions in the JSON, here is the attempt to not get a failure
        #Updated from emotion to emotion_dictionary
        return emotion_dictionary
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    app.run(debug=True)