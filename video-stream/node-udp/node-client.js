// Code ripped from https://www.sourcecodester.com/tutorials/11062/writing-udp-clientserver-application-nodejs.html
const dgram = require("dgram");
const client = dgram.createSocket("udp4");

const host = "0.0.0.0";
const port = 41100;

const message = new Buffer("Hello Server");

const parseTick = message => {
  const parts = message
    .toString()
    .split(",")
    .map(part => +part);
  return {
    price: parts[0],
    time: parts[1]
  };
};

let latestTickTime = -1;

client.on("message", (message, remote) => {
  const tick = parseTick(message);

  if (tick.time > latestTickTime) {
    console.log("Price is", tick.price);
    latestTickTime = tick.time;
  } else {
    console.log("Price is outdated, discard");
  }
});

client.send(message, 0, message.length, port, host, (err, bytes) => {
  if (err) {
    throw err;
  }

  console.log("Message sent");
});
