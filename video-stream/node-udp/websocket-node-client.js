const net = require("net");
const utf8 = require("utf8");
const fs = require("fs");

const HOST = "";
const PORT = 5100;
const message = utf8.encode("get");

var client = new net.Socket();
client.connect(PORT, HOST, function() {
  console.log("Connected");
  client.write(message);
});

client.on("data", function(data) {
  let jpg = Buffer.from(data.toString(), "base64");
  console.log("jpg", jpg);

  fs.writeFile(`${Math.random()}my-file.jpg`, jpg, err => {
    if (err) throw err;
    console.log("The binary data has been decoded and saved to my-file.png");
  });
  client.write(message);
});

client.on("close", function() {
  console.log("Connection closed");
});
