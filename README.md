# Genome

This project purpose is to deploy an application through a Docker container on a local machine or a server and make the applications ports accessible via a public IP address (if needed) by a chisel tunnel created by the app itself. So we need an active chisel server running for tunnel and the app which need to be run under genome container.

Dynamic docker deployment solution:
This app provides a method to deploy docker containers on demand

Services inside the container:

	-NodeJS http server
	-RDP server for remote desktop connections
	-Chisel tunnel to localhost

Open source libraries:
	
	- XRDP server image obtained from 
	  https://github.com/danielguerra69/ubuntu-xrdp
	
	- Chisel tcp tunnel obtained from
	  https://github.com/jpillora/chisel

How to use:

	Edit the config.json file to modify attributes, default attributes are given

	DOMAIN:
		-The domain on which the RDP server should be accessible

	SUBDOMAIN:
		-Subdomain for the above domain

	CHISEL_PORT:
		-Port number for hosting chisel server (No change needed)

	RDP_PORT:
		-The port on which the RDP server should be accessible

	CONTAINER_NAME:
		-The name of the docker container. Must be unique for each.

	NODEJS_PORT:
		-The port on which the NodeJS server should be accessible

	PASSWD: 
		-Password for RDP login

	LOCAL_CHISEL:
		-Specify 'yes' to run alongside a localmachine.
	
	APP_REPO_LINK:
		-Git repository for nodeJS app, to be downloaded and run in container.
	
	APP_FILE:
		-File name for nodeJS app.

	APP_DIR_NAME:
		-Directory to clone app into.

	Run on the server:
		$ chisel server --reverse

1. Run the install.py file
```
$python3 install.py
```


2. Run the run.py file
	
	$ python3 run.py

Directories and Files:

	- config.json:
		Configurations passed to the docker container at runtime.
	
	- autostart:
		Contains auto-logout configuration

	- bin:
		Contains binaries for logout and entrypoints

	- etc:
		Contains supervisor config (RDP)

	- run.py:
		Python script to run the container

	- docker-compose.yml:
		Docker compose build instructions config file
	
	- install.sh:
		Bash script to install python and dependencies	
	
	- requirements.txt:
		Dependencies for run.py

	- stop.py:
		Python script to stop running container	
	
Everytime to kill the running containers use:
```
Python3 stop.py
```
