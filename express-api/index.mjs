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