# AutoAvenue

AutoAvenue is a car dealership web application built with Flask, SQLAlchemy, Flask-RESTful, Flask-JWT-Extended, Cloudinary, and other technologies.

## Features

- **User Authentication**: Secure user registration and login using JWT authentication.
- **Car Management**: CRUD operations for managing cars, including image upload via Cloudinary.
- **Order Management**: Place and manage customer orders with various details.
- **Session Management**: Server-side session management for user interactions.
- **RESTful API**: Implements RESTful endpoints for flexible data retrieval and manipulation.

## Technologies Used

- Python 3
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended
- Flask-Bcrypt
- Cloudinary (for image management)
- SQLite (default, can be configured for other databases)

## Installation
`pipenv install`

### Clone the repository


- git clone 
- cd autoavenue
- pipenv install


# Run migrations 
- flask db init  # Initialize migrations (if not already initialized)
- flask db migrate -m "Initial migration"  # Create migration script
- flask db upgrade  # Apply migration to the database

# Run the application
- flask run


