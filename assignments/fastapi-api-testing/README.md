# 📘 Assignment: Testing FastAPI Endpoints with Pytest

## 🎯 Objective

Learn how to write automated tests for a FastAPI application using `pytest` and `TestClient`. By the end of this assignment, students will verify API behavior for successful requests and common error cases.

## 📝 Tasks

### 🛠️ Set Up the Test Environment

#### Description
Use the provided FastAPI starter application and create a test file that can run with `pytest`.

#### Requirements
Completed program should:

- Import `TestClient` from `fastapi.testclient` and the `app` object from `starter-code.py`.
- Create a reusable test client for the app.
- Run tests with `pytest` and confirm the test file is discovered.


### 🛠️ Test Successful API Responses

#### Description
Write tests for endpoints that should return valid data when called correctly.

#### Requirements
Completed program should:

- Test `GET /` and verify status code `200`.
- Test `GET /items` and verify response is a JSON list.
- Test `GET /items/{item_id}` with a valid ID and verify expected fields in the response.


### 🛠️ Test Error Handling

#### Description
Write tests for invalid requests so students can verify the API handles errors correctly.

#### Requirements
Completed program should:

- Test `GET /items/{item_id}` with a missing ID and verify status code `404`.
- Test `POST /items` with invalid payload data and verify validation error status code.
- Use clear assertion messages so failed tests are easy to understand.
