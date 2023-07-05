from flask import Flask,request
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def main():
    if request.method=="POST":
        inp=request.form.get("inp")
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(inp)
        if score["neg"]!=0:
            return "negative"
        else:
            return "positive"
            
if __name__=='__main__':
    app.run(debug=True)