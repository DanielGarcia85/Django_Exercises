# Parcel Management API

This project is a Django REST API for managing parcel deliveries. It was created as part of the course ***65-41 Interschool Software Development*** at **Haute École de Gestion (HEG)**.

## Features
- **RESTful API** built with **Django REST framework** for managing orders and products.
- **Authentication**: Only authenticated users can create orders.
- **CRUD Operations**: Supports creating, reading, updating, and deleting orders and products.
- **Admin Panel** for managing data.
- **Serialization** with **Django REST Framework serializers**.

## Project Structure
- **parcel_project/** : Main Django project directory.
- **parcel_manager/** : Django app for managing orders and products. Contains the models, views, serializers, and API logic.
- **db.sqlite3** : SQLite database.
- **manage.py** : Django management script.

## Prerequisites
- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework** (DRF)
- **pip** (Python package manager)
- **Virtual environment** (`venv` recommended)

## Installation
Set up the project with the following commands:

- Create and activate a virtual environment
```shell
python -m venv env
env\Scripts\activate.bat  # Windows
source env/bin/activate  # Mac/Linux
```
- Install Django and Django REST Framework
```shell
pip install django
pip install django djangorestframework
```
- Initialize Django project and app
```shell
django-admin startproject parcel_project .
django-admin startapp parcel_manager
```
- Apply database migrations
```shell
python manage.py migrate
```
- Create a superuser
```shell
python manage.py createsuperuser --email admin@example.com --username admin
```
- Run the development server
```shell
python manage.py runserver
```

## Models
The project contains two main models:

### Product
| Field      | Description                       | Type         | Constraints                  |
|------------|-----------------------------------|--------------|------------------------------|
| id         | Unique identifier of the product  | Integer      | Auto-incremented primary key |
| name       | Name of the product               | CharField    | Required, Max 200 chars      |
| brand      | Brand of the product              | CharField    | Required, Max 200 chars      |
| price      | Price of the product              | DecimalField | Required                     |


### Order
| Field       | Description                        | Type         | Constraints                                |
|-------------|------------------------------------|--------------|--------------------------------------------|
| id          | Unique identifier of the order     | Integer      | Auto-incremented primary key               |
| date        | Date when the order was placed     | DateField    | Auto-generated                             |
| sender      | Name of the sender                 | CharField    | Max 200 chars                              |
| destination | Name of the destination            | CharField    | Max 200 chars                              |
| weight      | Weight of the parcel               | DecimalField | Default: 1.0                               |
| status      | Status of the order                | CharField    | Choices: Confirmed, In Delivery, Delivered |
| product     | Product associated with the order  | ForeignKey   | Linked to Product model                    |

## API Endpoints
| Method | Endpoint             | Description                       | Authentication |
|--------|----------------------|-----------------------------------|----------------|
| GET    | `/api/orders/`       | Get all orders                    | ❌ No         |
| POST   | `/api/orders/`       | Create a new order                | ✅ Yes        |
| GET    | `/api/orders/{id}/`  | Retrieve a single order by ID     | ❌ No         |
| PUT    | `/api/orders/{id}/`  | Update an order                   | ✅ Yes        |
| DELETE | `/api/orders/{id}/`  | Delete an order                   | ✅ Yes        |
| GET    | `/api/products/`     | Get all products                  | ❌ No         |
| POST   | `/api/products/`     | Create a new product              | ✅ Yes        |
| GET    | `/api/products/{id}/`| Retrieve a single product by ID   | ❌ No         |
| PUT    | `/api/products/{id}/`| Update a product                  | ✅ Yes        |
| DELETE | `/api/products/{id}/`| Delete a product                  | ✅ Yes        |
| POST   | `/api-auth/login/`   | Connexion (DRF)                   | ❌ No         |
| DELETE | `/api-auth/logout/`  | Déconnexion                       | ✅ Yes        |


## Testing
To test the API, visit the Django REST Framework browsable API at:
- Orders: http://127.0.0.1:8000/api/orders/
- Products: http://127.0.0.1:8000/api/products/
- Admin Panel: http://127.0.0.1:8000/admin/

## Useful References
- Django REST Framework: https://www.django-rest-framework.org/
- Django Documentation: https://docs.djangoproject.com/en/stable/

## License
This project is licensed under the Creative Commons Attribution-ShareAlike (CC BY-SA) license.

## Author
Project created by Daniel Garcia as part of the course ***65-41 Interschool Software Development*** at **Haute École de Gestion (HEG)** during the Spring semester of 2025.
