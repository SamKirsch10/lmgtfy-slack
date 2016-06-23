# lmgtfy-slack

This simple WSGI listens for a ``/lmgtfy [statement]`` slack slash command and returns that statement as a lmgtfy.com search (hidden as a bit.ly shortened link). Currently written in python, the only requirements are falcon, gunicorn, and pyshorteners.

### Installation
* pip install falcon
* pip install gunicorn
* pip install pyshorteners

### Usage
    $ sudo gunicorn -b 0.0.0.0:80 wsgi:app
The above will start the simple server. The use of sudo allows you to bind to port 80. If you want to use a different port, sudo shouldn't be nessesary (and also change the port you want after the -b toggle). In your slack custom integrations, point a /lmgtfy slash command to send to your domain.

### Changelog
6.23.2016 - currently works by replying as a bot user with your link. Working to change that so it will reply in your original message.