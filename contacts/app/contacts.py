from flask import Flask, render_template, request, abort, redirect, url_for
from model import db, save_db

app = Flask(__name__)

@app.route("/")
def home():
  return render_template(
         "index.html",
          contacts=db
          
    )

@app.route("/contact/<int:index>")
def contact_view(index):
    try:
        contact = db[index]
        return render_template("contact.html", contacts=db, contact=contact, index=index, max_index=len(db)-1)
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

@app.route("/add_contact", methods=['POST','GET'])
def add_contact():
   if request.method == "POST":
      next_primary_key = db[len(db)-1]["pk"] + 1
      contact = {"pk": next_primary_key, 
                 "model": "addressbook.Contact",
                 "fields": 
                  {"city": request.form['city'],
                    "first_name": request.form['firstname'],
                    "last_name": request.form['surname'],
                    "zip": request.form['zip'],
                    "title": request.form['title'],
                    "address1": request.form['address1'],
                    "address2": request.form['address2'],
                    "address3": request.form['address3'],
                    "mi": "", 
                    "fax": "",
                    "email": request.form['email'],
                    "phone": request.form['telephone'],
                    "state": request.form['state'],
                    "country": request.form['country'],
                    "notes": "", 
                    "grad_class": ""
                  }
                }
      db.append(contact)
      save_db()
      return redirect(url_for("contact_view", index=len(db)-1))
   else:
      return render_template("add_contact.html",contacts=db)