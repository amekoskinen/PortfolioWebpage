from flask import Flask, render_template
import os
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap=Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET")



class ContactForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = StringField(label="Your Email", validators=[DataRequired()])
    subject = StringField(label="Subject", validators=[DataRequired()])
    message= TextAreaField(label="Message", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
@app.route("/contact")
def contact():
    form = ContactForm()
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
