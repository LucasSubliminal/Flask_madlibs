from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    """Generate questions to be asked"""
    #Defines variable prompts and gets the story var in stories.py
    prompts = story.prompts
    #Renders template "questions" with variables defined above
    return render_template("questions.html", prompts=prompts)

@app.route('/story')
def show_results():
    """Show the results of user's choices"""
    #Gets the users input from the form
    text = story.generate(request.args)
    #Returns a rendered HTML page with variables above
    return render_template("story", text==text)

