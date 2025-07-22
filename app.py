from flask import Flask, render_template, redirect, flash, url_for
from forms import SubscriptionForm

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        return redirect(url_for("subscribe"))
    return render_template("subscribe.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
