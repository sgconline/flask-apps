from flask import Flask, render_template, request, abort, redirect, url_for
from model import get_all_contacts, get_contact, add_contact, delete_contact

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    contacts = get_all_contacts()
    return render_template("index.html", contacts=contacts)

@app.route("/contact/<contact_id>")
def contact_view(contact_id):
    contacts = get_all_contacts()
    contact = get_contact(contact_id)
    if not contact:
        abort(404)
    # Find index and max_index for navigation
    ids = [str(c["_id"]) for c in contacts]
    try:
        index = ids.index(contact_id)
    except ValueError:
        abort(404)
    max_index = len(contacts) - 1
    return render_template("contact.html", contacts=contacts, contact=contact, index=index, max_index=max_index, ids=ids, contact_id=contact_id)

@app.route('/remove_contact/<contact_id>', methods=["GET", "POST"])
def remove_contact_route(contact_id):
    contact = get_contact(contact_id)
    contacts = get_all_contacts()
    if not contact:
        abort(404, "Contact with an ID of {} not found.".format(contact_id))
    if request.method == "POST":
        delete_contact(contact_id)
        return redirect(url_for('home'))
    else:
        return render_template("remove_contact.html", contact=contact, contacts=contacts)

@app.route("/add_contact", methods=['POST','GET'])
def add_contact_route():
    contacts = get_all_contacts()
    if request.method == "POST":
        contact = {
            "title": request.form['title'],
            "first_name": request.form['firstname'],
            "last_name": request.form['surname'],
            "email": request.form['email'],
            "phone": request.form['telephone'],
            "address1": request.form['address1'],
            "address2": request.form['address2'],
            "address3": request.form['address3'],
            "city": request.form['city'],
            "zip": request.form['zip'],
            "state": request.form['state'],
            "country": request.form['country']
            
        }
        new_id = add_contact(contact)
        return redirect(url_for("contact_view", contact_id=new_id))
    else:
        return render_template("add_contact.html", contacts=contacts)

@app.route("/edit_contact/<contact_id>", methods=["GET", "POST"])
def edit_contact_route(contact_id):
    contact = get_contact(contact_id)
    contacts = get_all_contacts()
    if not contact:
        abort(404)
    if request.method == "POST":
        updated_data = {
            "first_name": request.form.get("first_name", contact.get("first_name", "")),
            "last_name": request.form.get("last_name", contact.get("last_name", "")),
            "title": request.form.get("title", contact.get("title", "")),
            "email": request.form.get("email", contact.get("email", "")),
            "phone": request.form.get("phone", contact.get("phone", "")),
            "address1": request.form.get("address1", contact.get("address1", "")),
            "address2": request.form.get("address2", contact.get("address2", "")),
            "address3": request.form.get("address3", contact.get("address3", "")),
            "city": request.form.get("city", contact.get("city", "")),
            "zip": request.form.get("zip", contact.get("zip", "")),
            "state": request.form.get("state", contact.get("state", "")),
            "country": request.form.get("country", contact.get("country", "")),
            # Add other fields as needed
        }
        from model import update_contact
        update_contact(contact_id, updated_data)
        return redirect(url_for("contact_view", contact_id=contact_id))
    else:
        return render_template("edit_contact.html", contact=contact, contacts=contacts)
