# FastAPI Task Management API

## Project Overview

This project is a simple Task Management REST API built using **FastAPI**, **PostgreSQL**, and **psycopg2**. It demonstrates CRUD (Create, Read, Update, and Delete) operations on a PostgreSQL database.

## Technologies Used

- Python 3
- FastAPI
- PostgreSQL
- psycopg2
- Pydantic
- Uvicorn

## Project Structure

```
FASTAPI_Psycopg2_DB/
│── main.py
│── database.py
│── models.py
│── requirements.txt
│── README.md
│── .gitignore
```

## Database

Database Name:

```
taskdb
```

Table:

```sql
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE
);
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Example Request (POST)

```json
{
  "title": "Learn FastAPI",
  "is_completed": false
}
```

## Example Response

```json
{
  "message": "Task created successfully",
  "id": 1,
  "title": "Learn FastAPI",
  "is_completed": false
}
```

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FASTAPI_Psycopg2_DB.git
```

Move into the project folder

```bash
cd FASTAPI_Psycopg2_DB
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

## Author

Created as part of a FastAPI and PostgreSQL CRUD assignment using psycopg2.