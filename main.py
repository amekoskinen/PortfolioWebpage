from flask import Flask, render_template, request, url_for
import os
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired
import smtplib

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
print(my_email)
print(password)


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
@app.route("/contact", methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject: {subject}!\n\nName: {name}\nEmail: {email}\nMessage:\n{message}")
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
