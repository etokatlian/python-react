import React from "react";
import ReactDOM from "react-dom";

const App = () => (
  <div>
    <h1>App</h1>
  </div>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
