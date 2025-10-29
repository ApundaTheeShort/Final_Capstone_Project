# Hostel Booking System

A comprehensive web application for managing hostel bookings, room inventory, user authentication, and role-based access control. This project is built using Django REST Framework and MySQL, fully containerized with Docker for easy deployment.

## Overview

The Hostel Booking System is a full-featured REST API application that enables educational institutions to manage their hostel facilities, rooms, and booking requests. The system supports three distinct user roles (admin, custodian, and student) with different permission levels, providing a complete workflow from room creation to booking approval.

## Key Features

### User Management
*   Email-based authentication system (uses email instead of username)
*   Custom user model with three roles: **admin**, **custodian**, and **student**
*   User registration with role assignment
*   Profile management
*   Token-based and session-based authentication
*   Role-based permissions and access control

### Hostel Management
*   Create, view, update, and delete hostel facilities (admin only)
*   Assign custodians to manage specific hostels
*   Track hostel capacity, location, and descriptions
*   Filter hostels by name, location, or custodian
*   Different data visibility based on user roles

### Room Management
*   Create and manage rooms within hostels (custodian/admin)
*   Three room types: single, double, suite
*   Track room availability and pricing per semester
*   Prevent duplicate room numbers within the same hostel
*   Advanced filtering and search capabilities
*   Role-specific serializers for data security

### Booking System
*   Students can create booking requests for available rooms
*   Booking status workflow: pending → approved/rejected
*   Custodians and admins can approve or reject bookings
*   Date validation (check-out must be after check-in)
*   Prevents double-booking of rooms
*   Students can only view their own bookings
*   Custodians/admins have full visibility of all bookings

### Advanced Features
*   RESTful API architecture
*   Custom permission classes for fine-grained access control
*   Dynamic serializer selection based on user roles
*   Comprehensive filtering, searching, and ordering
*   Pagination support (10 items per page)
*   Custom exception handling with authentication redirects
*   Dockerized development environment
*   Database management UI (Adminer)

## Technologies Used

*   **Backend Framework:** Django 5.2.7
*   **API Framework:** Django REST Framework 3.16.1
*   **Database:** MySQL 8.0 with mysqlclient 2.2.7
*   **Authentication:** Token & Session-based authentication
*   **Filtering & Search:** django-filter 24.2
*   **Containerization:** Docker & Docker Compose
*   **Database UI:** Adminer
*   **Environment Management:** python-dotenv 1.1.1
*   **Language:** Python 3.10

## System Architecture

### User Roles & Permissions

The system implements three distinct user roles with specific permissions:

| Role | Permissions | Capabilities |
|------|------------|--------------|
| **Admin** | Full system access | Manage hostels, rooms, users, and all bookings |
| **Custodian** | Hostel management | Manage rooms in assigned hostels, approve/reject bookings |
| **Student** | Limited access | Create bookings, view own bookings, browse available rooms |

### Database Models

#### CustomUser
*   Email-based authentication (primary key)
*   Fields: email, first_name, last_name, role, date_joined, is_active
*   Custom manager for email authentication

#### Hostel
*   UUID primary key
*   Fields: name, location, capacity, description, custodian_id (FK to CustomUser)
*   Timestamps: created_at, updated_at
*   Validation: Custodian must have 'custodian' role

#### Room
*   UUID primary key
*   Fields: room_number, room_type (single/double/suite), price_per_semester, hostel (FK), is_available
*   Timestamps: created_at, updated_at
*   Unique constraint: (hostel, room_number)

#### Booking
*   UUID primary key
*   Fields: student_id (FK), room_id (FK), check_in_date, check_out_date, status (pending/approved/rejected)
*   Timestamps: created_at, updated_at
*   Unique constraint: (student_id, room_id)
*   Validation: Check-out date must be after check-in date, no double-booking

## API Endpoints

### Authentication
*   `POST /api/login/` - User login (session-based)
*   `POST /api/logout/` - User logout
*   `POST /api/register/` - User registration
*   `GET /api/profile/` - View user profile (requires authentication)
*   `POST /api/api-token-auth/` - Generate authentication token

### User Management
*   `GET /api/users/` - List all users (requires custodian or admin role)

### Hostels
*   `GET /api/hostels/` - List all hostels (authenticated users)
*   `POST /api/hostels/` - Create new hostel (admin only)
*   `GET /api/hostels/<uuid:pk>/` - Retrieve specific hostel
*   `PUT/PATCH /api/hostels/<uuid:pk>/` - Update hostel (admin only)
*   `DELETE /api/hostels/<uuid:pk>/` - Delete hostel (admin only)

**Filtering:** `?name=<value>&location=<value>&custodian_id=<uuid>`
**Search:** `?search=<query>` (searches name, location)
**Ordering:** `?ordering=created_at` or `?ordering=-name`

### Rooms
*   `GET /api/rooms/` - List all rooms (authenticated users)
*   `POST /api/rooms/` - Create new room (custodian or admin)
*   `GET /api/rooms/<uuid:pk>/` - Retrieve specific room
*   `PUT/PATCH /api/rooms/<uuid:pk>/` - Update room (custodian or admin)
*   `DELETE /api/rooms/<uuid:pk>/` - Delete room (custodian or admin)

**Filtering:** `?room_type=<single|double|suite>&is_available=<true|false>&hostel=<uuid>&price_per_semester=<value>`
**Search:** `?search=<query>` (searches room_number, hostel name)
**Ordering:** `?ordering=price_per_semester` or `?ordering=-created_at`

### Bookings
*   `GET /api/bookings/` - List bookings (students see only their own, custodians/admins see all)
*   `POST /api/bookings/` - Create new booking (student only)
*   `GET /api/bookings/<uuid:pk>/` - Retrieve specific booking
*   `PUT/PATCH /api/bookings/<uuid:pk>/` - Update booking status (custodian or admin)
*   `DELETE /api/bookings/<uuid:pk>/` - Delete booking (custodian or admin)

**Filtering:** `?status=<pending|approved|rejected>&room_id=<uuid>&student_id=<uuid>`
**Search:** `?search=<query>` (searches student username, room number)
**Ordering:** `?ordering=created_at` or `?ordering=check_in_date`

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

### Web Interface
*   **Register:** Navigate to `/accounts/register/` to create a new user account
*   **Login:** Navigate to `/accounts/login/` to log in
*   **Profile:** After logging in, access your profile at `/accounts/profile/`
*   **Logout:** Use the logout button in the navigation bar
*   **Admin Panel:** Access the Django admin panel at `http://localhost:8000/admin/` using your superuser credentials

### API Usage Examples

#### 1. Get Authentication Token
```bash
curl -X POST http://localhost:8000/api/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user@example.com", "password": "yourpassword"}'
```

Response:
```json
{
  "token": "your-auth-token-here"
}
```

#### 2. List Available Rooms (with filtering)
```bash
curl -X GET "http://localhost:8000/api/rooms/?is_available=true&room_type=single" \
  -H "Authorization: Token your-auth-token-here"
```

#### 3. Create a Booking (as student)
```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Authorization: Token your-auth-token-here" \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": "room-uuid-here",
    "check_in_date": "2025-01-15",
    "check_out_date": "2025-06-15"
  }'
```

#### 4. Approve a Booking (as custodian/admin)
```bash
curl -X PATCH http://localhost:8000/api/bookings/booking-uuid-here/ \
  -H "Authorization: Token your-auth-token-here" \
  -H "Content-Type: application/json" \
  -d '{"status": "approved"}'
```

#### 5. Create a New Hostel (as admin)
```bash
curl -X POST http://localhost:8000/api/hostels/ \
  -H "Authorization: Token your-auth-token-here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "North Campus Hostel",
    "location": "North Wing, Building A",
    "capacity": 200,
    "description": "Modern hostel facilities",
    "custodian_id": "custodian-user-uuid"
  }'
```

#### 6. List Your Bookings (as student)
```bash
curl -X GET "http://localhost:8000/api/bookings/?status=pending" \
  -H "Authorization: Token your-auth-token-here"
```

### Pagination
All list endpoints support pagination. Navigate through pages using:
```bash
# First page (default)
GET /api/rooms/

# Specific page
GET /api/rooms/?page=2

# Results show: {"count": 50, "next": "...", "previous": "...", "results": [...]}
```

## Project Structure

```
Final_Capstone_Project/
├── accounts/                   # User authentication & management
│   ├── models.py              # CustomUser model
│   ├── serializers.py         # User serializers
│   ├── views.py               # Auth views
│   ├── permissions.py         # Custom permission classes
│   ├── urls.py                # Auth routes
│   └── templates/             # HTML templates
├── hostels/                   # Hostel & room management
│   ├── models.py              # Hostel & Room models
│   ├── serializers.py         # Multiple serializers (role-based)
│   ├── views.py               # Hostel & Room viewsets
│   └── urls.py                # Hostel/Room routes
├── bookings/                  # Booking management
│   ├── models.py              # Booking model
│   ├── serializers.py         # Booking serializers
│   ├── views.py               # Booking viewsets
│   └── urls.py                # Booking routes
├── hostel_booking_system/     # Main project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL router
│   ├── exception_handler.py   # Custom exception handling
│   └── wsgi.py                # WSGI config
├── docker-compose.yml         # Docker services configuration
├── Dockerfile                 # Python/Django container
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
└── README.md                  # This file
```

## Common Workflows

### For Students
1. Register an account with role="student"
2. Get authentication token via `/api/api-token-auth/`
3. Browse available rooms: `GET /api/rooms/?is_available=true`
4. Create a booking: `POST /api/bookings/` with room_id and dates
5. Check booking status: `GET /api/bookings/`
6. Wait for custodian/admin approval

### For Custodians
1. Receive custodian account from admin
2. Get assigned to a hostel by admin
3. Create rooms in your hostel: `POST /api/rooms/`
4. Manage room availability
5. Review booking requests: `GET /api/bookings/?status=pending`
6. Approve/reject bookings: `PATCH /api/bookings/<id>/`

### For Admins
1. Create superuser account (Django admin)
2. Create hostels: `POST /api/hostels/`
3. Create custodian accounts and assign to hostels
4. Oversee all bookings and rooms
5. Manage system users via `/api/users/`

## Security Considerations

*   All API endpoints require authentication (except registration)
*   Token-based authentication for API access
*   Session-based authentication for web interface
*   Role-based access control (RBAC) enforced at the view level
*   Custom permission classes prevent unauthorized access
*   UUID primary keys prevent enumeration attacks
*   Password validation enforced (minimum 9 characters)
*   Custom exception handler redirects unauthorized users to login
*   Environment variables for sensitive configuration
*   HTTPS/HSTS enforced in production settings

## Development Notes

### Running Management Commands
```bash
# Make migrations
docker-compose run --rm backend python manage.py makemigrations

# Apply migrations
docker-compose run --rm backend python manage.py migrate

# Create superuser
docker-compose run --rm backend python manage.py createsuperuser

# Open Django shell
docker-compose run --rm backend python manage.py shell
```

### Viewing Logs
```bash
# View all container logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f backend
```

### Stopping and Cleaning Up
```bash
# Stop containers
docker-compose down

# Stop and remove volumes (WARNING: deletes database)
docker-compose down -v

# Rebuild containers
docker-compose up --build
```

### Database Access
Access the database via Adminer at `http://localhost:8080/` or connect directly:
```bash
docker-compose exec db mysql -u hostel_user -p hostel_db
```

## Troubleshooting

### Common Issues

**Issue:** Container fails to start with "port already in use"
**Solution:** Change the port mapping in `docker-compose.yml` or stop the service using the port

**Issue:** Database connection refused
**Solution:** Wait for the database health check to pass. Check with `docker-compose ps`

**Issue:** "No such table" errors
**Solution:** Run migrations inside the container:
```bash
docker-compose run --rm backend python manage.py migrate
```

**Issue:** Authentication errors
**Solution:** Ensure you're using email (not username) for login and include the token in headers:
```bash
Authorization: Token your-token-here
```

**Issue:** Permission denied errors
**Solution:** Verify your user role matches the required permission for the endpoint

## Testing

Run tests inside the Docker container:
```bash
docker-compose run --rm backend python manage.py test
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact & Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## Acknowledgments

*   Built with Django and Django REST Framework
*   Containerized with Docker for easy deployment
*   Implements industry-standard authentication and authorization patterns
