import threading
import requests
import os
import time, json, datetime

total_thread = os.cpu_count()
time.sleep(1)
loop = 1
def push_rank():
	auth = open("auth.txt", "r")
	headers = {
	'authorization':auth.read()
	}
	while loop == 1:
		jam = datetime.datetime.now()
		req = requests.get('http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/2', headers=headers)
		response = json.loads(req.text)
		print('[{}-{}-{} {}:{}:{}] SUCCESS |TROPI: {} |MAHKOTA: {}'.format(jam.year, jam.month, jam.day, jam.hour, jam.minute, jam.second, response['User']['SkillRating'], response['User']['Crowns']))
		time.sleep(0.5)


for i in range(1, total_thread + 1):
    t = threading.Thread(target=push_rank)
    t.start()