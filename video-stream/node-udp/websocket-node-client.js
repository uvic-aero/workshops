const net = require("net");
const utf8 = require("utf8");

const HOST = "";
const PORT = 5100;
const message = utf8.encode("get");

var client = new net.Socket();
client.connect(PORT, HOST, function() {
  console.log("Connected");
  client.write(message);
});

client.on("data", function(data) {
  console.log(data);
  client.write(message);
});

client.on("close", function() {
  console.log("Connection closed");
});
