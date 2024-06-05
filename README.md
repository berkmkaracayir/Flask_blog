# Flask_blog

#### Introduction

This is a Flask-based blog application that allows users to register, log in, create, edit, and delete blog posts. Admin users have additional capabilities to manage other users.

#### Project Structure

The project directory contains the following files and directories:

- `app.py`: Main application file to run the Flask server.
- `docker-compose.yaml`: Docker Compose file to set up and run the application.
- `Dockerfile`: Dockerfile for building the Docker image.
- `init_db.py`: Script to initialize the database.
- `login.py`: Script for user login functionality.
- `register_user.py`: Script for user registration via CLI.
- `schema.sql`: SQL file to create the database schema.
- `requirements.txt`: List of Python dependencies.
- `templates/`: Directory containing HTML template files.
- `static/`: Directory containing static files like CSS and JavaScript.
- `README.md`: This file.

#### Installation

To run this application locally, follow these steps:

**Using Docker Compose:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/berkmkaracayir/Flask_blog.git
   cd Flask_blog
   ```

2. **Build and run the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Initialize the database:**
   ```bash
   docker-compose exec web python init_db.py
   ```

**Without Docker Compose:**

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables and run the application:**
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=production
   flask run
   ```

5. **Initialize the database:**
   ```bash
   python init_db.py
   ```

#### Usage

Once the application is running, you can access it at `http://localhost:8000`.

1. **Register a new user:**
   - Access the registration page at `http://localhost:8000/register` or use the CLI script:
     ```bash
     docker-compose exec web python register_user.py
     ```

2. **Log in:**
   - Access the login page at `http://localhost:8000/login`.

3. **Create a new post:**
   - Access the create post page at `http://localhost:8000/create`.

4. **Edit a post:**
   - Go to the specific post page and click the "Edit" button if you are the owner or an admin.

5. **Delete a post:**
   - Go to the specific post page and click the "Delete" button if you are the owner or an admin.

6. **Admin panel:**
   - Admin users can access the admin panel at `http://localhost:8000/admin` to manage users.

#### Endpoints

The following table lists the key endpoints of the application along with their HTTP methods and descriptions:

| Endpoint             | Method | Description                              |
|----------------------|--------|------------------------------------------|
| `/`                  | GET    | Home page listing all blog posts.        |
| `/post/<post_id>`    | GET    | View a specific post.                    |
| `/create`            | GET    | Display the form to create a new post.   |
| `/create`            | POST   | Submit a new post.                       |
| `/edit/<post_id>`    | GET    | Display the form to edit a post.         |
| `/edit/<post_id>`    | POST   | Submit changes to a post.                |
| `/delete/<post_id>`  | POST   | Delete a post.                           |
| `/login`             | GET    | Display the login form.                  |
| `/login`             | POST   | Submit login credentials.                |
| `/logout`            | GET    | Log out the current user.                |
| `/register`          | GET    | Display the registration form.           |
| `/register`          | POST   | Submit registration details.             |
| `/admin`             | GET    | Admin panel for managing users.          |
| `/edit_user/<id>`    | GET    | Display the form to edit a user.         |
| `/edit_user/<id>`    | POST   | Submit changes to a user.                |
| `/delete_user/<id>`  | POST   | Delete a user.                           |

#### File Descriptions

1. **`app.py`**:
   - The main Flask application file that initializes and runs the server.

2. **`docker-compose.yaml`**:
   - Defines the services for the Docker Compose setup. It builds the web service and maps port 8000.

3. **`Dockerfile`**:
   - Contains instructions to build the Docker image for the application.

4. **`init_db.py`**:
   - Script to initialize the SQLite database using the schema defined in `schema.sql`.

5. **`login.py`**:
   - Handles user login functionality.

6. **`register_user.py`**:
   - CLI script for registering a new user, specifically an admin user.

7. **`schema.sql`**:
   - SQL script to create the necessary database tables.

8. **`requirements.txt`**:
   - Lists all the Python packages required to run the application.

9. **`templates/`**:
   - Contains the HTML templates for different pages:
     - `base.html`: Base template extended by other templates.
     - `index.html`: Home page listing all blog posts.
     - `post.html`: Individual post page.
     - `create.html`: Create a new post page.
     - `edit.html`: Edit an existing post page.
     - `login.html`: User login page.
     - `register.html`: User registration page.
     - `edit_user.html`: Edit user information page.
     - `admin.html`: Admin dashboard.

10. **`static/`**:
    - Contains static files like CSS and JavaScript.

#### Dependencies

The project requires the following Python packages (listed in `requirements.txt`):
- Blinker
- Click
- Flask
- Flask-Login
- Flask-WTF
- Gunicorn
- Itsdangerous
- Jinja2
- Markdown
- Markdown2
- MarkupSafe
- Packaging
- Werkzeug
- WTForms

#### License

This project is licensed under the MIT License.

---

Feel free to contribute to the project by submitting pull requests or reporting issues. For detailed information on usage and contributing guidelines, refer to the documentation within the project repository.
