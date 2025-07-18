# 🐾 Shelter Management System

A RESTful backend application for managing animal shelter operations, including animal profile listings and adoption request workflows. Built with Django and Django REST Framework (DRF).

---

## 🚀 Features

### 🔐 Admin Features
- **Animal Profile Management**
  - Create, update, delete animal profiles.
  - Track species, breed, age, health status, and adoption status.
- **Adoption Request Management**
  - View all submitted adoption requests.
  - Approve or reject requests based on eligibility.

### 👥 User Features
- **Browse Animal Profiles**
  - View detailed, read-only animal information.
  - Filter/search by species, breed, etc.
- **Submit Adoption Requests**
  - Submit a request for adoption.
  - View the status of your submitted requests (Pending, Approved, Rejected).

---

## 🔄 Adoption Workflow

1. Users browse available animals.
2. Users submit adoption requests.
3. Admins review and approve/reject requests.
4. Approved users receive confirmation and next steps.

---

## 🧱 API Endpoints

| Method | Endpoint                         | Description                                  | Access   |
|--------|----------------------------------|----------------------------------------------|----------|
| POST   | `/api/signup/`                   | Register a new user                          | Public   |
| POST   | `/api/login/`                    | Authenticate user and receive token          | Public   |
| GET    | `/api/animals/`                  | List all animal profiles                     | User     |
| POST   | `/api/adoption-requests/`        | Submit an adoption request                   | User     |
| GET    | `/api/adoption-requests/`        | List all adoption requests                   | Admin    |
| GET    | `/api/adoption-requests/{id}/`   | View details of a specific request           | Admin/User |
| PATCH  | `/api/adoption-requests/{id}/`   | Approve or reject an adoption request        | Admin    |

---

## 🧩 Models

### 🐶 Animal
| Field          | Type     | Description              |
|----------------|----------|--------------------------|
| species        | String   | Species of the animal    |
| breed          | String   | Breed of the animal      |
| age            | Integer  | Age in years             |
| health_status  | String   | Medical condition/status |
| adoption_status| Enum     | Available / Adopted      |
| created_at     | DateTime | Record creation time     |
| modified_at    | DateTime | Last update time         |

### 📄 AdoptionRequest
| Field  | Type   | Description                          |
|--------|--------|--------------------------------------|
| user   | FK     | Linked user submitting the request   |
| animal | FK     | Animal being adopted                 |
| status | Enum   | Pending / Approved / Rejected        |

---

## 🏛️ Apps Structure


---

## 🔐 Role-Based Access Control (RBAC)

- **Admin**: Can manage animal profiles and adoption requests.
- **User**: Can view animals and submit/view their own adoption requests.

---

## ⚙️ Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- Token-based Authentication

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone <repo-url>
cd shelter-management

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
