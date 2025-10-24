# Hostel Booking System

A web application for managing hostel bookings, user authentication, and profiles. This project is built using Django and MySQL, containerized with Docker.

## Features

*   User Registration and Authentication (Login/Logout)
*   User Profiles
*   Custom User Model with roles (admin, custodian, student)
*   REST API endpoints (using Django Rest Framework)
*   Dockerized development environment

## Technologies Used

*   **Backend:** Django (Python)
*   **Database:** MySQL
*   **API:** Django Rest Framework
*   **Containerization:** Docker, Docker Compose

## Setup Instructions

Follow these steps to get the project up and running on your local machine using Docker.

### Prerequisites

*   Docker Desktop (or Docker Engine and Docker Compose) installed on your system.

### 1. Clone the Repository

```bash
git clone <repository_url>
cd Final_Capstone_Project
```

### 2. Environment Variables

Create a `.env` file in the root of the project directory (where `docker-compose.yml` is located) and add the following environment variables. Replace the placeholder values with your desired credentials.

```env
DJANGO_SECRET_KEY='your_secret_key_here'
MYSQL_DATABASE='hostel_db'
MYSQL_USER='hostel_user'
MYSQL_PASSWORD='hostel_password'
MYSQL_ROOT_PASSWORD='root_password'
DB_HOST='db'
```

### 3. Build and Run Docker Containers

Build the Docker images and start the services defined in `docker-compose.yml`.

```bash
docker-compose up --build -d
```

This command will:
*   Build the `backend` (Django) service.
*   Start the `db` (MySQL) service.
*   Start the `adminer` (database management UI) service.
*   Run them in detached mode (`-d`).

Wait for a few moments for the database to become healthy. You can check the status with `docker-compose ps`.

### 4. Apply Database Migrations

Once the containers are running and the `db` service is healthy, apply the database migrations. This must be done *inside* the `backend` container.

```bash
docker-compose run --rm backend python manage.py makemigrations accounts
docker-compose run --rm backend python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

Create an administrator account to access the Django admin panel.

```bash
docker-compose run --rm backend python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

### 6. Access the Application

The Django development server will be running inside the `backend` container.

*   **Django Application:** Open your web browser and go to `http://localhost:8000/`
*   **Adminer (Database UI):** Open your web browser and go to `http://localhost:8080/`
    *   **System:** MySQL
    *   **Server:** `db` (this is the service name in `docker-compose.yml`)
    *   **Username:** `hostel_user` (or whatever you set in `.env`)
    *   **Password:** `hostel_password` (or whatever you set in `.env`)
    *   **Database:** `hostel_db` (or whatever you set in `.env`)

## Usage

*   **Register:** Navigate to `/accounts/register/` to create a new user account.
*   **Login:** Navigate to `/accounts/login/` to log in.
*   **Profile:** After logging in, you can access your profile at `/accounts/profile/`.
*   **Logout:** Use the logout button in the navigation bar.
*   **Admin Panel:** Access the Django admin panel at `http://localhost:8000/admin/` using your superuser credentials.

## Contributing

Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
