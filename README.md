
# Phone Directory API Documentation

## Overview
The Phone Directory API is a RESTful service that allows users to manage personal contacts, report spam numbers, and search for contacts by name or phone number. The API is designed for mobile application consumption, providing a secure and user-friendly interface for managing contacts and spam reports.

## Features
- User registration and authentication
- Manage personal contacts (CRUD operations)
- Mark numbers as spam
- Search contacts by name and phone number
- Secure access to all endpoints

## Technologies Used
- **Framework**: Django
- **Database**: SQLite (for development)
- **REST Framework**: Django REST Framework (DRF)
- **Authentication**: Token-based authentication

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Step-by-step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nameisluv/phone_directory_api.git
   cd phone_directory_api
   ```
   or
   
   **Download the repository as a ZIP file and extract it.**
    ```bash
    cd phone_directory_api
    ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install django djangorestframework djangorestframework.authtoken
   ```
   can install through requirments.txt also

5. **How to Generate Fake Data**
    - Run the Management Command present in (api/management/commands/populate_data.py
): 
      ```bash
      python manage.py populate_data
      ```
    - This will generate fake data for the `User` and `Contact` models.

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### User Registration
- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@example.com",
        "password": "yourpassword"
    }
    ```
- **Response**: Returns the user details upon successful registration.

### User Login
- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "phone_number": "1234567890",
        "password": "yourpassword"
    }
    ```
- **Response**: Returns an authentication token if login is successful.

### Manage Contacts
#### List Contacts
- **Endpoint**: `/api/contacts/`
- **Method**: `GET`
- **Authentication Required**: Yes

#### Create Contact
- **Endpoint**: `/api/contacts/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "Jane Doe",
        "phone_number": "0987654321"
    }
    ```

#### Retrieve Contact
- **Endpoint**: `/api/contacts/<contact_id>/`
- **Method**: `GET`
- **Authentication Required**: Yes

#### Update Contact
- **Endpoint**: `/api/contacts/<contact_id>/`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "name": "Jane Smith",
        "phone_number": "0987654321"
    }
    ```

#### Delete Contact
- **Endpoint**: `/api/contacts/<contact_id>/`
- **Method**: `DELETE`
- **Authentication Required**: Yes

### Mark Spam
- **Endpoint**: `/api/mark_spam/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "contact_number": "1234567890"
    }
    ```
- **Authentication Required**: Yes

### Search Contacts by Name
- **Endpoint**: `/api/search/name/`
- **Method**: `GET`
- **Query Parameter**: `query` (string to search for)

### Search Contacts by Phone Number
- **Endpoint**: `/api/search/phone/`
- **Method**: `GET`
- **Query Parameter**: `query` (phone number to search for)

## Testing
You can test the API using tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/). Make sure to include the authentication token in the headers for protected endpoints.

## Conclusion
This API provides a comprehensive solution for managing contacts and reporting spam, with a focus on security and usability. For further improvements, consider implementing additional features such as user profile management, enhanced search capabilities, and a more robust spam detection mechanism.
