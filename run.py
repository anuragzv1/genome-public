#@Tanay Karve
import json
import yaml
import os
import sys

with open("config.json","r") as jFile:
    jData=jFile.read()
    jData=json.loads(jData)
    
with open("docker-compose.yml","r") as cFile:
    yData=(yaml.safe_load(cFile))


domain=jData["DOMAIN"]
subdomain=jData["SUBDOMAIN"]
hostport=str(jData["CHISEL_PORT"])
port=jData["RDP_PORT"]
passwd=jData["PASSWD"]
local=jData["LOCAL_CHISEL"]
name=jData["CONTAINER_NAME"]
nodejsPort=jData["NODEJS_PORT"]
appRepoLink=jData["APP_REPO_LINK"]
appFile=jData["APP_FILE"]
appDir=jData["APP_DIR_NAME"]

if local not in ["yes","no"]:
    print("Error in config file: LOCAL must be either yes or no")
    sys.exit(-1)

if (type(port)) != int:
    print("Error in config file: PORT must be an integer")
    sys.exit(-1)


os.system("docker run -d --name "+name+" --hostname terminalserver --shm-size 1g -p "+str(port)+":3389 -p 2244:22 -p "+str(nodejsPort)+":3000 danielguerra/ubuntu-xrdp")
cmd="docker exec -ti "+name+" /bin/bash -c \"echo -e \\\""+passwd+"\n"+passwd+"\n\n\n\\\" | (passwd ubuntu)\""
os.system("docker exec uxrdp-node /bin/bash -c \" cd ~ && git clone "+appRepoLink+" "+appDir+"\"")  
 
os.system("docker exec -ti "+name+" /bin/bash -c \"cd ~/"+appDir+"/ && pm2 start "+appFile+"\"")
os.system(cmd)

if(local=="yes"):
    os.system("docker exec "+name+" /bin/bash -c \"chisel client http://"+subdomain+"."+domain+":"+hostport+" R:"+str(port)+":localhost:3389 R:"+str(nodejsPort)+":localhost:3000\"")
	
