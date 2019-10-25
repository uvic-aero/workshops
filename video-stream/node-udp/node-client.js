// Code ripped from https://www.sourcecodester.com/tutorials/11062/writing-udp-clientserver-application-nodejs.html
const dgram = require("dgram");
const client = dgram.createSocket("udp4");
const utf8 = require("utf8");
const fs = require("fs");

const HOST = "0.0.0.0";
const PORT = 5100;

const message = utf8.encode("get");

client.on("message", (message, remote) => {
  console.log(remote.address + ":" + remote.port + " - ");

  let jpg = Buffer.from(message, "base64");
  fs.writeFile(`${Math.random()}my-file.jpg`, jpg, err => {
    if (err) throw err;
    console.log("The binary data has been decoded and saved to my-file.png");
  });
});

client.send(message, 0, message.length, PORT, HOST, (err, bytes) => {
  if (err) throw err;
  console.log("UDP message sent to " + HOST + ":" + PORT);
});
