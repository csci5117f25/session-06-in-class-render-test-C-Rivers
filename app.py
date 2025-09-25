from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)
db.setup()

@app.route("/", methods=["GET"])
def view_guestbook():
    entries = db.get_guestbook()
    return render_template("hello.html", entries=entries)

@app.route("/add", methods=["POST"])
def add_entry():
    name = request.form.get("name")
    message = request.form.get("message")
    db.add_post(name, message)
    return redirect(url_for("view_guestbook"))