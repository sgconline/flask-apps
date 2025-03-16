from flask import Flask, render_template, request, abort, redirect, url_for
from model import db, save_db

app = Flask(__name__)

@app.route("/")
def home():
  return render_template(
         "index.html",
          contacts=db,
    )

@app.route("/contact/<int:index>")
def contact_view(index):
    try:
        contact = db[index]
        return render_template("contact.html", contact=contact, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route('/remove_contact/<int:index>', methods=["GET", "POST"])
def remove_contact(index):
  try:
    if request.method == "POST":
        del db[index]
        save_db()
        return redirect(url_for('home'))
    else:  
        return render_template("remove_contact.html", contact=db[index])
  except IndexError:
    abort(404)