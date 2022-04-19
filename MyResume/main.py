from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import smtplib
import os


my_email = os.environ.get("EMAIL")
p = os.environ.get("PASSWORD")



port_cont = [{""}, {"name": "Instagram Bot",
                    "category": "App",
                    "client": "Personal Project",
                    "date": "November 2021",
                    "url": "Github",
                    "description": "Automated Instagram Follower Bot written with Python Script",
                    "image": "InstagramBot"},
             {"name": "Blog",
              "category": "Web",
              "client": "Personal Project",
              "date": "April 2022",
              "url": "www.wojm-blog.herokuapp.com",
              "description": "Functional Blog with backend built using Flask", "image": "Blog"},
             {"name": "Cheap Flight Tracker",
              "category": "App",
              "client": "Personal Project",
              "date": "December 2021",
              "url": "Github",
              "description": "Automated Flight Bot written with Python Script to find cheapest flights from my location to my destination bucket-list",
              "image": "Flight"},
             {"name": "Data Analysis",
              "category": "Data",
              "client": "Personal Project",
              "date": "March 2022",
              "url": "Github",
              "description": "Analyzed hospital data set to support the theory that washing hands reduces the chances of getting bacterial infections",
              "image": "data science"},
             {"name": "Web-based Movie Library",
              "category": "Web",
              "client": "Personal Project",
              "date": "February 2022",
              "url": "Github",
              "description": "Personalized movie library built with python and Flaskv",
              "image": "Movie"}]
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def send_email(name, phone, email, message):
    send_message = f"Subject:Portfolio Message from {name}: A reader\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, p)
        connection.sendmail(msg=send_message, from_addr=my_email, to_addrs=my_email)


class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email Address")
    phone = StringField("Phone Number")
    message = StringField("Message")
    submit = SubmitField("Send Message")


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.name.data)
        send_email(form.name.data, form.phone.data, form.email.data, form.message.data)
    return render_template("index.html", form=form)


@app.route("/portfolio-details?<int:index>")
def portfolio(index):
    content = port_cont[index]

    return render_template("portfolio-details.html", post=content)


if __name__ == "__main__":
    app.run(debug=True)
