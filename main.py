import smtplib
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from form import MyForm

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "cabbagehead"

my_email = "cairns.python@gmail.com"
password = "Lionheart93"

email_to = "cairns.python@gmail.com"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = MyForm()
    if form.validate_on_submit():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # makes connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_to,
                                msg=f"Subject:New Contact\n\nName: {request.form['name']}"
                                    f"\n Email: {request.form['email']}"
                                    f"\n Phone: {request.form['phone']}"
                                    f"\n Description: {request.form['description']}".encode("utf8"))
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)