"""
Flask application that serves as a simple HTTP server with multiple endpoints.
This is a Python 3 rewrite of the original Node.js Express.js server,
preserving all features and functionality exactly.

Endpoints:
    GET /              -> Returns "Hello, World!\n" (text/plain, 200)
    GET /good-evening  -> Returns "Good evening" (text/html, 200)
    Other routes       -> 404 Not Found
"""

from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Port configuration matching the original Node.js server
PORT = 3000


@app.after_request
def set_security_headers(response):
    """
    Apply security headers to all responses.
    Mirrors the Express.js middleware that sets X-Content-Type-Options: nosniff
    and disables the X-Powered-By header (Flask does not send X-Powered-By by default).
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


@app.route('/', methods=['GET'])
def hello_world():
    """
    Root endpoint that returns the Hello World greeting.
    Preserves the exact behavior of the original Node.js server:
    - Response body: "Hello, World!\n" (with trailing newline)
    - Content-Type: text/plain
    - Status code: 200
    """
    return Response('Hello, World!\n', status=200, content_type='text/plain; charset=utf-8')


@app.route('/good-evening', methods=['GET'])
def good_evening():
    """
    Good evening endpoint that returns a greeting.
    Matches the Express.js endpoint behavior:
    - Response body: "Good evening"
    - Content-Type: text/html (Express default for res.send with string)
    - Status code: 200
    """
    return Response('Good evening', status=200, content_type='text/html; charset=utf-8')


if __name__ == '__main__':
    print(f'Server running at http://localhost:{PORT}/')
    app.run(host='0.0.0.0', port=PORT, debug=False)
