# Task Manager API

A Flask-based API for managing tasks, featuring JWT authentication, CRUD operations, and PostgreSQL integration. Deployed on Render.

## Features:
- **User Authentication**: JWT-based signup and login
- **CRUD Operations**: Create, read, update, and delete tasks
- **Database**: PostgreSQL
- **Deployment**: Render (Free Tier)

## API Endpoints:
- **POST `/register`**: Register a new user
- **POST `/login`**: Login and get JWT token
- **POST `/tasks`**: Create a task (JWT required)
- **GET `/tasks`**: List all tasks (JWT required)
- **PUT `/tasks/<task_id>`**: Update a task (JWT required)
- **DELETE `/tasks/<task_id>`**: Delete a task (JWT required)

## Deployment:
This project is deployed on Render.

## License
MIT License
