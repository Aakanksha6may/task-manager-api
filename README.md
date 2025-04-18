# Task Manager API

A simple, secure, and efficient **Task Manager API** built with **Flask**, using **JWT authentication**, and connected to a **PostgreSQL** database. This API allows users to manage tasks with complete CRUD operations.

---

## 🛠 Tools & Technologies

- **Flask**: A lightweight WSGI web application framework in Python, used for building the API.
- **PostgreSQL**: A powerful open-source database used to store user and task data.
- **JWT (JSON Web Tokens)**: Used for secure authentication to ensure that only authorized users can perform actions on their tasks.
- **Flask-SQLAlchemy**: A Flask extension for SQLAlchemy, allowing easy interaction with PostgreSQL.
- **Flask-JWT-Extended**: Provides JWT support for Flask, making it easy to handle authentication.
- **python-dotenv**: For managing environment variables such as database credentials and secret keys.
- **Render**: The app is deployed on Render's cloud platform for easy, hassle-free hosting.
- **VS Code**: The preferred code editor used for development and debugging.
- **pgAdmin**: A powerful management tool for PostgreSQL, used for database management and querying.

---

## 🎯 Features

- **User Authentication**: Secure login and signup using JWT tokens.
- **Task Management**: Create, read, update, and delete tasks with proper authentication.
- **PostgreSQL Database**: Efficient data storage for users and tasks.
- **Secure Routes**: Tasks-related operations are accessible only to authenticated users.
- **RESTful API**: Followed REST principles for API development.

---

## 🔧 How It Works

1. **User Authentication**:
   - Users can register and log in, receiving a JWT token for authentication.
   - This token is used in the request headers for subsequent task-related operations.
   
2. **Task Operations**:
   - **Create**: Authenticated users can add tasks.
   - **Read**: Users can view their own tasks.
   - **Update**: Users can modify existing tasks.
   - **Delete**: Users can remove tasks from the database.

---

## 🔩 API Endpoints

- **POST `/register`**: User signup (create a new user).
- **POST `/login`**: User login (generate a JWT token).
- **POST `/tasks`**: Create a new task (JWT required).
- **GET `/tasks`**: Retrieve all tasks for the authenticated user (JWT required).
- **PUT `/tasks/<task_id>`**: Update a specific task (JWT required).
- **DELETE `/tasks/<task_id>`**: Delete a specific task (JWT required).

---

## 💻 Installation

To set up and run the project locally:

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd task-manager-api
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    SECRET_KEY=your_flask_secret
    JWT_SECRET_KEY=your_jwt_secret
    DATABASE_URL=postgresql://username:password@localhost:5432/taskmanagerdb
    ```

5. **Initialize the database**:
    ```bash
    python
    >>> from app import app, db
    >>> with app.app_context():
    >>>     db.create_all()
    ```

6. **Run the app**:
    ```bash
    python app.py
    ```

---

## 🌍 Deployment

The app is deployed on **Render**. You can access it live via the following link:
- [Task Manager API on Render](<https://task-manager-api-xdoj.onrender.com>)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
