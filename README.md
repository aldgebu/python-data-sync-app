Python Developer Task App

This is a simple Python backend app built for a developer task.
It uses Docker Compose for easy setup with a PostgreSQL database and a Python backend.

Quick Start:

1. Clone the repository:
git clone <your-repo-url>
cd <your-project-directory>

2. Start the app using Docker Compose:
docker compose up

That’s it! The backend and database will start automatically.

API Documentation:

Once the app is running, you can explore all available API endpoints at:
http://localhost:5000/swagger

Ports & Configuration:

By default, the app requires:
- PostgreSQL: your local port 5432 → maps to the database container
- Python backend: your local port 5000 → maps to the backend container

Note: If either port is already in use on your machine, you should modify the .env file:
- Change DATABASE_PORT_LOCAL for the database port.
- Change APP_PORT_LOCAL for the backend port.

Requirements:
- Docker Compose to be installed
