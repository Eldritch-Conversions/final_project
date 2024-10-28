from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector 

app = Flask(__name__)

#Was getting a 404 error when I launched the application in the built in browser, attempting to fix that error with this
#@app.route('/')
#def home(EmotionDetection):
    #return "Welcome to the Emotion Detection API. Use the /emotionDetector endpoint for analysis."


#Original script prior to error noted above
@app.route('/emotionDetector', methods=['POST'])
def emotion_detection():
    data = request.get_json() 
    text_to_analyze = data.get("text")

    result = emotion_detector(text_to_analyze)

    #Format
    formatted_response = (
        f"For the given statement, the system response is " 
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return JSON response
    return jsonify({"message": formatted_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
