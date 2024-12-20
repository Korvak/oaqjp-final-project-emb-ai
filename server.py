from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("My app")

@app.route("/emotionDetector")
def emotion_detection():
    '''uses IBM emotion analyzer to analyze the passed text '''
    try :
        text_to_analyze = request.args.get('textToAnalyze')

        # Pass the text to the sentiment_analyzer function and store the response
        response = emotion_detector(text_to_analyze)

        if response["dominant_emotion"] is None:
            return "Invalid text! Please try again!"

        #we do a complicated formatting of the response dict because.. reasons
        response_txt = "For the given statement, the system response is "
        emotions = sorted( response.keys() )
        emotions.remove("dominant_emotion") #we add it later and don't want it in the mix
        for x in range(0,len(emotions)-1):
            response_txt += f"'{emotions[x]}' : {response[emotions[x]]}, "
        #we add the last emotion
        response_txt.strip(", ")
        response_txt += f"and '{emotions[-1]}' : {response[emotions[-1]]}. "
        response_txt += "The dominant emotion is "+response["dominant_emotion"]

        return response_txt
    except Exception as e :
        print(e)
        return "An error occurred while trying to handle the request. Please try again!", 500

@app.route("/")
def render_index_page():
    '''renders the index page in the static folder '''
    return render_template("index.html")

if __name__ == "__main__":
    #we run the server on the specified host and port
    app.run(host="0.0.0.0", port=5000)
