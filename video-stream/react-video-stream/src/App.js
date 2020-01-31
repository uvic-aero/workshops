import React, { useState, useEffect } from "react";
import WebSocket from "ws";

function App() {
  const [imgSrc, setSrc] = useState("");

  useEffect(() => {
    const WS_URL = "ws://localhost/video-stream";
    const ws = new WebSocket(WS_URL);
    ws.onopen = () => console.log(`Connected to ${WS_URL}`);
    ws.onmessage = message => {
      // set the base64 string to the src tag of the image
      setSrc(message.data);
    };
  });

  return (
    <div className="App">
      <img src={imgSrc} className="App-logo" alt="logo" />
    </div>
  );
}

export default App;
