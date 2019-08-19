from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def form_template():
    """Return homepage with form template"""
    
    prompts = story.prompts
    
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def create_story():
    """Show rendered story""" 

    story_text = story.generate(request.args)

    return render_template("story.html", story_text=story_text)
