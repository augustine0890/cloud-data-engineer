#!/bin/sh
sudo su
apt-get -y update
apt-get -y install nginx
echo "Hello, World!" > /var/www/html/index.html