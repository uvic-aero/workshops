// Code ripped from https://www.sourcecodester.com/tutorials/11062/writing-udp-clientserver-application-nodejs.html
const dgram = require("dgram");
const server = dgram.createSocket("udp4");

const host = "0.0.0.0";
const port = 41100;

const clients = [];

server.on("error", err => {
  console.log(err.stack);
  server.close();
});

server.on("message", (msg, rinfo) => {
  console.log(`Connected client at ${rinfo.address}:${rinfo.port}`);
  clients.push(rinfo);
});

server.on("listening", () => {
  const address = server.address();
  console.log(`server listening ${address.address}:${address.port}`);
});

setInterval(() => {
  const price = Math.floor(1000 + Math.random() * 100);
  const time = Date.now();
  const data = new Buffer(price + "," + time);

  clients.forEach(rinfo => {
    server.send(
      data,
      0,
      data.length,
      rinfo.port,
      rinfo.address,
      (err, bytes) => {
        if (err) {
          console.log(err.stack);
        }
      }
    );
  });
}, 1000);

server.bind(port, host);
