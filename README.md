# Flask Superheroes API

## Overview
This is a RESTful API built using Flask that allows users to interact with superheroes and their powers. The API provides endpoints to fetch heroes, powers, and associate powers with heroes.

## Features
- Retrieve a list of heroes.
- Retrieve a single hero by ID.
- Retrieve a list of powers.
- Retrieve a single power by ID.
- Update power details.
- Assign powers to heroes.

## Technologies Used
- Flask
- SQLAlchemy
- Python

## Application Structure

    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    └── server
        ├── app.py
        ├── instance
        │   └── superheros.db
        ├── migrations
        │   ├── alembic.ini
        │   ├── env.py
        │   ├── README
        │   ├── script.py.mako
        │   └── versions
        │       └── 44f19c1bb858_adds_models.py
        ├── models.py
        └── seed.py

## Setup and Installation
### Prerequisites
- Python 3
- Flask
- Flask-SQLAlchemy

### Installation Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd superheroes-flask
   ```
2. Install dependencies and open python virtual envirnoment:
   ```sh
    pipenv install && pipenv shell
   ```
3. Configure the FLASK_APP and FLASK_RUN_PORT environment variables:
    ```sh
    export FLASK_APP=app.py
    export FLASK_RUN_PORT=5555
    ```
4. Change directory:
   ```sh
    cd server
   ```
5. Run the app:
   ```sh
    flask run
   ```

## API Endpoints

### 1. Health Check
- **Endpoint:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {"message": "app running"}
  ```

### 2. Get All Heroes
- **Endpoint:** `/heroes`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {"id": 1, "name": "Spider-Man", "super_name": "Peter Parker"},
    {"id": 2, "name": "Iron Man", "super_name": "Tony Stark"}
  ]
  ```

### 3. Get Hero by ID
- **Endpoint:** `/heroes/<int:hero_id>`
- **Method:** `GET`
- **Response:**
  ```json
    {
        "id": 1,
        "name": "Kamala Khan",
        "super_name": "Ms. Marvel",
        "hero_powers": [
            {
            "hero_id": 1,
            "id": 1,
            "power": {
                    "description": "gives the wielder the ability to fly through the skies at supersonic speed",
                    "id": 2,
                    "name": "flight"
            },
            "power_id": 2,
            "strength": "Strong"
            }
        ]
    }
  ```
  **Error Response:**
  ```json
  {"error": "Hero not found"}
  ```

### 4. Get All Powers
- **Endpoint:** `/powers`
- **Method:** `GET`
- **Response:**
  ```json
    [
        {
            "description": "gives the wielder super-human strengths",
            "id": 1,
            "name": "super strength"
        },
        {
            "description": "gives the wielder the ability to fly through the skies at supersonic speed",
            "id": 2,
            "name": "flight"
        },
        {
            "description": "allows the wielder to use her senses at a super-human level",
            "id": 3,
            "name": "super human senses"
        },
        {
            "description": "can stretch the human body to extreme lengths",
            "id": 4,
            "name": "elasticity"
        }
    ]
  ```

### 5. Get Power by ID
- **Endpoint:** `/powers/<int:id>`
- **Method:** `GET`
- **Response:**
  ```json
    {
        "description": "gives the wielder super-human strengths",
        "id": 1,
        "name": "super strength"
    }
  ```
  **Error Response:**
  ```json
  {"error": "Power not found"}
  ```

### 6. Update Power Details
- **Endpoint:** `/powers/<int:id>`
- **Method:** `PATCH`
- **Request Body:**
  ```json
    {
        "description": "Valid Updated Description"
    }
  ```
- **Response:**
  ```json
    {
        "description": "Valid Updated Description",
        "id": 1,
        "name": "super strength"
    }
  ```
  **If power doesnt exist, Error Response:**
  ```json
  {"error": "Power not found"}
  ```
  **If validation does not pass, Error Response:**
  ```json
    {
        "errors": ["validation errors"]
    }
  ```

### 7. Assign Power to Hero
- **Endpoint:** `/hero_powers`
- **Method:** `POST`
- **Request Body:**
  ```json
    {
        "strength": "Average",
        "power_id": 1,
        "hero_id": 3
    }
  ```
- **Response:**
  ```json
    {
        "id": 11,
        "hero_id": 3,
        "power_id": 1,
        "strength": "Average",
        "hero": {
            "id": 3,
            "name": "Gwen Stacy",
            "super_name": "Spider-Gwen"
        },
        "power": {
            "description": "gives the wielder super-human strengths",
            "id": 1,
            "name": "super strength"
        }
    }
  ```
  **Error Response:**
  ```json
    {
        "errors": ["validation errors"]
    }
  ```

## Running Tests
You can test the API using tools like Postman.

## License
This project is licensed under the MIT License.

