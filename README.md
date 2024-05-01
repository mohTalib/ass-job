# Ass-Job

Ass-Job is a project aimed at implementing a task designed to assess software development skills, particularly with Python, FastAPI, SocketIO, and Tortoise ORM.

## Overview

The project consists of building a system with the following features:

1. **Token-based Authentication:** Implementing token-based authentication for both FastAPI and SocketIO, allowing users to register, log in, and receive JWT tokens upon successful authentication. Secure the SocketIO connection using these tokens to ensure only authenticated users can access real-time features.

2. **Advanced User Interaction and Notifications:** Creating a multi-role system with user roles like "Secretary," "Doctor," and "Laboratory." Implementing relationships between users with different roles using Tortoise ORM. Allowing doctors to send patient information to other doctors, with a notification system to alert doctors when they receive patient information from other doctors.

3. **Code Quality:** Ensuring clean, well-organized, and documented code. Prioritizing readability and maintainability.

## Setup

1. Install required dependencies: Django, FastAPI, SocketIO, and Tortoise ORM.
2. Set up the project structure and configure databases and project settings.
3. Run the project locally for development and testing.

## Usage

1. Register as a new user with a valid role (Secretary, Doctor, or Laboratory).
2. Log in using your registered credentials to access the system.
3. Perform actions based on your role, such as sending patient information (for doctors) or receiving notifications (for all roles).

## Project Structure

The project structure follows a modular design, with separate modules for routes, models, schemas, etc.:

ass-job/
│
├── app/
│   ├── routes/
│   │   ├── users.py
│   │   ├── doctors.py
│   │   ├── patients.py
│   │   └── ...
│   ├── models.py
│   ├── schemas.py
│   └── ...
│
├── main.py
├── requirements.txt
└── ...

## Contributing

Contributions to Ass-Job are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
