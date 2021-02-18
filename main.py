from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__) #Create App
app.secret_key = "thisisthemostsecretkeyever" # Website's Secret Key

# Application Configuration
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="eol.nuha22@gmail.com", # Here is your gmail
    MAIL_PASSWORD="*******", # your gmail's password
)
mail = Mail(app)

@app.route("/", methods=["POST", "GET"])
@app.route("/portofolio", methods=["POST", "GET"])
def home():
    if request.method == "POST": # POST method
        # get input values from form
        name = request.form["first"]
        lastname = request.form["last"]
        email = request.form["email"]
        phone = request.form["tel"]
        message = request.form["message"]
        msg = Message(
                name + " " + lastname, # Email Title
                sender="eol.nuha22@gmail.com",
                recipients=["eol.nuha22@gmail.com", email],) # Email recipients
        msg.body = "Greetings"
        msg.html = render_template(
                "contactmsg.html", name=name, lastname=lastname, email=email, phone=phone, message=message
                  )
        mail.send(msg)
        flash(f"Sent") #Inside template messages
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) #run App
