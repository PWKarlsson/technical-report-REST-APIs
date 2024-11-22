# Node.js with Express vs. Flask
The purpose of this report is to compare two popular framworks for building REST APIs, Node.js with Express (JavaScript-based) and Flask (Python-based). It will go through their setup processes, how they are built, their pros and cons and when to use which framework.
## Node.js with Express
### Setup
#### 1. Install Node.js and create a new project

```
mkdir express-api
cd express-api
npm init -y
npm install express
```

#### 2. Create API
   
```
touch index.mjs (if you use .js instead of .mjs you need to add 'type: module' in your package-json for Node.js to treat it as an ES module).
```

```
//index.mjs

import express from 'express';

const app = express();
const port = 1337;

app.use(express.json());

let items = [{ id: 1, name: 'Item 1'}]

app.get('/items', (req, res) => {
    res.json(items);
});
app.post('/items', (req, res) => {
    const item = { id: items.length + 1, name: req.body.name };
    items.push(item)
    res.status(201).json(item)
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

#### 3. Start the API

```
node index.mjs
```

#### 4. Test the API (new terminal window)
##### Fetch all items

```
curl -X GET http://localhost:1337/items
```

##### Expected response

```
[{"id":1, "name":"Item 1"}]
```

##### Add a new item

```
curl -X POST http://localhost:1337/items -H "Content-Type: application/json" -d '{"name": "Item 2"}'
```

##### Expected response

```
[{"id":1, "name":"Item 1"},{"id:2, "name":"Item 2"}]
```

---
## Flask
### Setup
#### 1. Make sure that you have Python installed, then install Flask

```
pip install flask
```

#### 2. Create a new project

```
mkdir flask-api
cd flask-api
```

#### 3. Create API

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

#### 4. Start the api

```
python3 app.py
```

#### 5. Test the API (new terminal window)
##### Fetch all items

```
curl -X GET http://127.0.0.1:5000/items
```

##### Expected response

```
[
   {
      "id":1,
      "name": "Item 1"
   }
]
```

##### Add a new item

```
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name": "Item 2"}'
```

##### Expected response

```
[
   {
      "id":1,
      "name": "Item 1"},
   {
      "id:2,
      "name": "Item 2"
   }
]
```

---
## Comparison

| Aspects | Node.js (Express) | Flask |
| :-----: | :---------------: | :---: |
| Language | JavaScript       | Python |
| Fraemwork | Javascript web Framework | Python Web Framework |
| Platform | Built on V8 engine | CPython |
| Architecture | Event-driven, non blocking I/O | Web Server Gateway Interface |
| Cocurrency | Single threaded | Multi-threaded |
| Web server integration | Built in HTTP-server (e.g., http, Express) | Reuquires a separate web server (e.g., Apache, Nginx) |
| Learning curve | Somewhat steeper, requires knowledge of JavaScrip | Somewhat flatter, requires knowledge of Python which is an easier language to learn |

## Pros and Cons
### Node.js with Express
#### Pros:
   * Asynchronous, can handle multiple request at a time.
   * Large ecosystem of npm packages to utilize.
   * High scalability due to the non-blocking I/O model and event-driven archiecture.
#### Cons:
   * Steeper learning curve, requires knowledge of Node.js/JavaScript.
   * Higly depent on npm packages, you need to learn what you need.
   * Even though the asynchronus environment increases scalability, it can make the error handling trickier to cope with.

### Flask
#### Pros:
   * Python-based which is a simple and beginner-friendly language.
   * Supports template engines like Jinja2.
   * Integrates well with projects that involves data science or machine-learning.
#### Cons:
   * Synchronous by default, hadles one request at a time.
   * Lack of built-in features, often requires additional libraries.
   * Less suitable for javaScript-heavy stacks.

---
## Conclusion
Both Node.js with Express and Flask are great tools to use when it comes to building a REST API for your project. They both have their pros and cons relative to eachother and have their different use-cases. Node.js would be preferred if your project is built on a Javascript ecosysem, if it requires high performance and scalability or if you are in the need of a large library of pre-built packages.
Flask is a choice to consider if you are new to programming and lack knowledge about JavaScript/Node.js, if you are working on a machine-learning project, or if your project is not in need of high performance and/or scalability.
What method to choose for your project is highly dependent on your programming language knowledge and what type of project you are working on.

---
_Pontus Karlsson_
