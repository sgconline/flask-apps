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
 versions 
*   0.1 - 0.9 Nginx, Flask & Gunicorn were all running within a single Docker image, reading from a json file. 
*   1.0 - 1.7 Nginx was separated out into its own Dockerfile and subsequent image
*   2.0 - 2.2 Major version update as application rewritten to store user details in a MongoDB from a Json file and Bug fixes.
  
 ### Leaning Goals
* The learning goals which have been achieved are
   * Write a very basic Python Flask app. Which is a address book application which can add, remove and edit users from a json file.
   * Use Git & Github to version control the app. 
   * Create branches to add functionality to the app and merge with the main branch.
   * Upgrade application to use MongoDB using GitHub CoPilot 
   * Run the application as a container using Docker and then Kubernetes (MiniKube) 
      * Write a Dockerfile to image the three components of the application (web (nginx), app(Flask,Gunicorn), db(mongodb)) using the docker build command and upload to DockerHub. Add the created Dockerfile to the Git repo
      * Write a a Docker compose file to run the full application ensuring successful port forward ingress and egress from VirtualBox NatNetwork. Add the compose.yml files to the Git Repo
      * Write a K8s deployment file to run the full application creating the relevant Services to enable communication outside of the K8S Network and beyond the VirtualBox NatNetwork
   * The applicatiton exposed the correct https port and mongodb port for connecting external MongoDB Compass administration tool
   * Setup Nginx as a reverse http and tcp (stream) proxy on the MiniKube host to forward requests from out side of the NatNetwork, main my laptop which is the VirtualBox host
      *    To serve the Contacts Web Application. PortForward -  VirtualBox Host NatNetwork (loopback) -> MiniKube Nginx -> K8s NodePort -> Nginx RP -> Gunicorn Flask App -> MongoDB
      *    To administer the Contacts DB using MongoDB Compass. PortForward -  VirtualBox Host NatNetwork (loopback) -> MiniKube Nginx -> K8s NodePort -> MongoDB
