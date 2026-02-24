# hao-backprop-test

A simple Python 3 Flask HTTP server with multiple endpoints. This is a tutorial/test project demonstrating basic Flask routing and request handling, rewritten from the original Node.js Express.js implementation.

## Prerequisites

- Python 3.12+ (tested with Python 3.12.3)
- pip (Python package manager)

## Setup

Create a virtual environment and install the project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

Start the server:

```bash
python app.py
```

The server will start and listen on port `3000`. Access it at [http://localhost:3000/](http://localhost:3000/).

## Available Endpoints

| Endpoint | Method | Response | Content-Type |
|---|---|---|---|
| `/` | GET | `Hello, World!\n` | text/plain; charset=utf-8 |
| `/good-evening` | GET | `Good evening` | text/html; charset=utf-8 |

Any other route will return a `404 Not Found` response.

### Examples

```bash
# Hello World endpoint
curl http://localhost:3000/

# Good Evening endpoint
curl http://localhost:3000/good-evening
```

## Project Structure

| File | Purpose |
|---|---|
| `app.py` | Flask application with route handlers |
| `requirements.txt` | Python dependencies (Flask and transitive packages) |
| `README.md` | Project documentation |
