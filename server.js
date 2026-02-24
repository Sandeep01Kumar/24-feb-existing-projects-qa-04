const express = require('express');
const app = express();
const port = 3000;

// Disable X-Powered-By header to prevent server technology fingerprinting
app.disable('x-powered-by');

// Set X-Content-Type-Options header on all responses to prevent MIME type sniffing
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  next();
});

app.get('/', (req, res) => {
  res.type('text/plain').send('Hello, World!\n');
});

app.get('/good-evening', (req, res) => {
  res.send('Good evening');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
