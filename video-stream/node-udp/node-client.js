// Code ripped from https://www.sourcecodester.com/tutorials/11062/writing-udp-clientserver-application-nodejs.html
const dgram = require("dgram");
const client = dgram.createSocket("udp4");
const utf8 = require("utf8");
const WebSocket = require("ws");

const HOST = "0.0.0.0";
const PORT = 5100;

const message = utf8.encode("get");
const WS_URL = "ws://localhost:3001";
const ws = new WebSocket(WS_URL);

client.send(message, 0, message.length, PORT, HOST, (err, bytes) => {
  if (err) throw err;
  console.log("UDP message sent to " + HOST + ":" + PORT);
});

ws.onopen = () => {
  client.on("message", (message, remote) => {
    console.log(remote.address + ":" + remote.port + " - ");
    // let jpg = Buffer.from(message.toString(), "base64");
    let jpg = `data:image/jpeg;base64,${message.toString()}`;
    ws.send(jpg);
  });
};

// client.on("message", (message, remote) => {
//   console.log(remote.address + ":" + remote.port + " - ");
//   let jpg = Buffer.from(message.toString(), "base64");
//   ws.send(jpg);
//   fs.writeFile(`${Math.random()}my-file.jpg`, jpg, err => {
//     if (err) throw err;
//     console.log("The binary data has been decoded and saved to my-file.png");
//   });
// });
