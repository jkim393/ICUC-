var express = require("express"); //require returns a function as object
var app = express();
var http = require('http').Server(app); //send the express framework into the http server
var io = require('socket.io')(http);    //
var mongoose = require('mongoose');
mongoose.connect("mongodb://localhost/fuck_app");

var userSchema = new mongoose.Schema({
    email: String,
    name: String,
    pw: String,
    group: String
});

var groupSchema = new mongoose.Schema({
    email: String,
    name: String,
    pw: String,
    channel: String
});

var User = mongoose.model("User", userSchema);
var Group = mongoose.model("Group", groupSchema);

app.set("view engine", "ejs");

app.get("/", function(req, res){
   res.render("landing"); 
});

var numUsers = 0;


io.on('connection', function(socket){
  console.log("a user connected");
  var addedUser = false;

  //server sending message to client
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
  
  socket.on('messager name', function(nam){
    io.emit('messager name', nam);
  });
  
  socket.on('subscribe', function(room) { 
    console.log('joining room', room);
    socket.join(room); 
    io.emit('subscribe', room);
  });

  socket.on('unsubscribe', function(room) {  
    console.log('leaving room', room);
    socket.leave(room); 
  });
  
});
 
app.get("/", function(req, res){
   res.render("landing"); 
});

app.get("/signup", function(req, res){
   res.render("signup"); 
});

app.get("/login", function(req, res){
   res.render("login"); 
});

app.get("/message", function(req, res){
   res.render("message"); 
});


http.listen(process.env.PORT, process.env.IP, function(){
   console.log("Started Server"); 
});