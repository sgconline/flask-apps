# Python Application - Contacts App

This small python application was written to assist with my learning path. 

Collecting workspace informationThe contacts application is a simple Flask-based web application that functions as an address book.
Here's a summary of its functionality:
1. **Home Page (`/`)**:
   - Displays a list of contacts stored in the application.
   - Each contact is linked to a detailed view of the contact.

2. **Contact Details (`/contact/<int:index>`)**:
   - Displays detailed information about a specific contact, such as name, title, phone, email, and address.
   - Provides navigation to view the next contact or start over if the end of the list is reached.
   - Includes a link to remove the contact.

3. **Remove Contact (`/remove_contact/<int:index>`)**:
   - Allows users to delete a specific contact.
   - Displays a confirmation page before deletion.
   - If confirmed, the contact is removed from the database, and the user is redirected to the home page.

4. **Data Management**:
   - Contacts are stored in a JSON file (`db/addressbook_db.json`), which is loaded into memory when the application starts.
   - Changes to the contacts (e.g., deletions) are saved back to the JSON file using the `save_db` function.

5. **Templates**:
   - Uses Jinja2 templates to render HTML pages dynamically.
   - Includes templates for the home page, contact details, and contact removal confirmation.

6. **Error Handling**:
   - Handles invalid contact indices by returning a 404 error.

This application is a basic demonstration of Flask's capabilities, including routing, template rendering, and handling user input. It is suitable for learning purposes but not recommended for production use due to its reliance on a global in-memory database and lack of robust data validation or authentication.

The latest docker images of the application can be found at:
* https://hub.docker.com/repositories/sgconline
  * contacts-app - Flask Application fronted by gunicorn
  * contacts-web - Nginx reverse proxy to contacts-app gunicon instance.

 ### Previous Versions
