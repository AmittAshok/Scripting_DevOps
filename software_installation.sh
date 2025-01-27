#!/bin/bash
#
packages=( docker.io, nginx ,httpd )

 for package in "${packages[@]}" ; do
	 sudo apt-get install "$package" -y 
 done
