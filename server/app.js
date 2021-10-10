const express = require("express");
const app = express();
const path = require('path');


app.get("/api", (req, res) => {
  res.json({ message: "Hello from server!" });
});

app.use(express.static(path.resolve(__dirname, '../client/build')));

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});