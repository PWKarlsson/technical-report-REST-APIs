# Node.js with Express vs. Flask
The purpose of this report is to compare two popular framworks for building REST APIs, Node.js with Express (JavaScript-based) and Flask (Python-based). It will go through their setup processes and make a comparison of their pros and cons.
# Node.js with Express
## Setup
### 1. Install Node.js and create a new project

```
mkdir express-api
cd express-api
npm init -y
npm install express
```

### 2. Create API
   
```
touch index.js
```

```
//index.js

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

### 3. Start the API

```
node index.js
```

# Flask
## Setup
### 1. Make sure that you have Python installed, then install Flask

```
pip install flask
```

### 2. Create a new project

```
mkdir flask-api
cd flask-api
```

### 3. Create API

```
touch app.py
```

```
//app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

items = [{'id': 1, 'name': 'item 1'}]

@app.route('/items', methods=['GET'])
def get_items():
   return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
   new_item = {'id': len(items) + 1, 'name': request.json['name']}
   items.append(new_item)
   return jsonify(new_item), 201

if __name__ == '__main__':
   app.run(debug=True)
```

### 3. Start the api

```
python app.py
```

# Comparison

| Aspects | Node.js (Express) | Flask |
| ------- | ----------------- | ----- |
| Language | JavaScript       | Python |
| Fraemwork | Javascript web Framework | Python Web Framework |
| Platform | Built on V8 engine | CPython |
| Architecture | Event-driven, non blocking I/O | Web Server Gateway Interface |
| Cocurrency | Single threaded | Multi-threaded |
| Web server integration | Built in HTTP-server (e.g., http, Express) | Reuquires a separate web server (e.g., Apache, Nginx) |
| Learning curve | Somewhat steeper, requires knowledge of JavaScrip | Somewhat flatter, requires knowledge of Python which is an easier language to learn |

# Pros and Cons
## Node.js with Express
## * Pros:
   * Fast and asynchronous.
   * Lots of npm packages.
   * Works well for full-stack JavaScript project.
## * Cons:
   * Requires some knowledge of Node.js/JavaScript.
   * Lack of built-in features meaning you need to know what packages you need to install.
   * Steeper learning curve.

## Flask
## * Pros:
   * Python-based which is a simple and beginner-friendly language.
   * Supports template engines like Jinja2.
   * Integrate well with machine learning projects
## * Cons:
   * Synchronous by default, works better for lightweight projects.
   * 
