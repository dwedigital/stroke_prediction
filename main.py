from flask import Flask, render_template, request
from scripts import forms
from scripts.persona import Persona
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    form = forms.StrokeForm()
    return render_template('index.html', form =form)

@app.route('/',methods=['POST'])
def indexPost():
    # cast to dict so that you can change key:values in the class
    submission = request.form.to_dict()
    user = Persona(submission)
    prediction = user.Predict()
    form = forms.StrokeForm()

    return render_template('index.html', data = {
        "no":prediction['probabilities']['0.0'],
        "yes": prediction['probabilities']['1.0']
    }, form = form)

if __name__ =="__main__":
    app.run(debug=True,port=8000)