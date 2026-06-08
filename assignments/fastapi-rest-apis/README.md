# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework and practice core API concepts such as routes, request handling, and CRUD operations. By the end of this assignment, students will create and test an API that manages a small in-memory collection of items.

## 📝 Tasks

### 🛠️ Create the FastAPI App and First Endpoint

#### Description
Set up a FastAPI application and implement a basic health-check endpoint to confirm the server is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance in starter-code.py.
- Add a GET endpoint at `/` that returns a JSON message.
- Run with Uvicorn and respond successfully in a browser or API client.


### 🛠️ Add Read Endpoints for Item Data

#### Description
Implement endpoints that return all items and a single item by ID from an in-memory list.

#### Requirements
Completed program should:

- Store sample item data in a Python list.
- Add a GET endpoint at `/items` to return all items.
- Add a GET endpoint at `/items/{item_id}` to return one item.
- Return a clear error message when the item ID does not exist.


### 🛠️ Implement Create, Update, and Delete Endpoints

#### Description
Complete CRUD functionality by adding endpoints to create new items, update existing items, and delete items.

#### Requirements
Completed program should:

- Add a POST endpoint at `/items` to create a new item.
- Add a PUT endpoint at `/items/{item_id}` to update an item.
- Add a DELETE endpoint at `/items/{item_id}` to remove an item.
- Return meaningful JSON responses for success and failure cases.
