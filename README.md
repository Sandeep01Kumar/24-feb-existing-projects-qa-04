# hao-backprop-test

A simple Express.js HTTP server with multiple endpoints. This is a tutorial/test project demonstrating basic Express.js routing and request handling.

## Setup

Install the project dependencies:

```bash
npm install
```

## Running the Server

Start the server using the npm start script:

```bash
npm start
```

Or invoke the server directly:

```bash
node server.js
```

The server will start and listen on port `3000`. Access it at [http://localhost:3000/](http://localhost:3000/).

## Available Endpoints

| Endpoint | Method | Response | Content-Type |
|---|---|---|---|
| `/` | GET | `Hello, World!\n` | text/plain |
| `/good-evening` | GET | `Good evening` | text/html (Express default) |

### Examples

```bash
# Hello World endpoint
curl http://localhost:3000/

# Good Evening endpoint
curl http://localhost:3000/good-evening
```
