# Overview

This project was my attempt at working with servers and networking. Read a lot about sockets and threading and had some fun with it. It was pretty fun and an awesome experience when my second computer could interact with my first!

The program written is has two elements. The server and the client! The server will take in your IP address and a port and will take in clients who use the same IP address and port. Really it just displays the messages sent by anyone who is on the server as well as their IP address. The client side uses the IP address and port and connects to send messages back and forth with another client. What's pretty cool is I also took a stab at using a python gui library, tkinter! My first time ever using and it was pretty tough. Although rough I think the chat looks good.

My purpose for doing this project is to continue to expand my knowledge. Always wondered how others got started with these kind of chat rooms and now I know!

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The following project is a server client program because of the two scripts. There is one for servers and another for clients. Whichever IP address your computer running the server script runs ends up being the server that the clients connect to!

Since I'm using sockets and sending packets between the server and the clients this program usines the TCP protocol.


The format server side is "<\IP ADDRESS/>: {message}"
Client side the message format is "You: {message}" but when someone else sends a message it looks like this <\IP ADDRESS/>: {message}

# Development Environment

The tools used were definitely geeksforgeeks and youtube. Biggest help when it comes to being stumped.

The libraries I used were tkinter, sockets,threading as well as a scrolledtext library. The language this was written in was Python!
# Useful Websites


* [GeeksForGeeks](https://www.geeksforgeeks.org/)
* [Scrolled Text Video](https://www.youtube.com/watch?v=Z2gt28vryxo&t=312s&ab_channel=Tkinter%E2%80%A4com)
* [This tkinter tutorial](https://www.youtube.com/watch?v=epDKamC-V-8&ab_channel=CoreySchafer)
* [This Socket tutorial](https://www.youtube.com/watch?v=sUzM-vIC-s4&t=3s&ab_channel=RealPython)

# Future Work

* Nicer GUI
* Easier way to set up server and connect to it
* second page for gui to input ip and port