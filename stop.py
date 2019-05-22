import os
import json
with open("config.json","r") as jFile:
    jData=jFile.read()
    jData=json.loads(jData)
name=jData["CONTAINER_NAME"]

os.system("docker stop "+name+";docker rm "+name)

