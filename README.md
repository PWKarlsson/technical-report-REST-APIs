# Node.js with Express vs. Flask
The purpose of this report is to compare two popular framworks for building REST APIs, Node.js with Express (JavaScript-based) and Flask (Python-based). It will go through their setup processes and make a comparison of their pros and cons.
# Node.js with Express
## Setup
1. ### Install Node.js and create a new project

```
mkdir express-api
cd express-api
npm init -y
npm install express
```

2. ### Create API
   
```
touch index.js
cd index.js
```

```
import express from 'express';

const app = express();
const port = 1337;

app.use(express.json());

let item = [{ id: 1, name: 'Item 1'}]

app.get('/items', (req, res) => {
    res.json(items);
});
app.post('/items', (req, res) => {
    const item = { id: items.length + 1, req.body.name };
    items.push(item)
    res.status(201).json(item)
});

app.listen(port, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

3. ### Start the API

```
node index.js
```
