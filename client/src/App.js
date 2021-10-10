import './App.css';
import { useEffect } from "react";

function App() {

  useEffect(() => {
    fetch("api")
    .then(res => res.json())
    .then(console.log);
    console.log("IN");
  }, []);

  return (
    <div className="App">
      <p>WElcome To Dans project</p>
    </div>
  );
}

export default App;
