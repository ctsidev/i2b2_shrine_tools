import os
import requests
requests.packages.urllib3.disable_warnings()

def run_query(filename):
	with open(filename, 'r') as queryfile:
		data=queryfile.read()
		verify='CERT_NAME.crt.pem'
		url='https://URL:PORT/shrine20/shrine-webclient/'
		r = requests.post(url,data,verify=False)
		results=r.text
		fd = open('results/'+filename,'w')
                fd.write(results)
                fd.close()

for fn in os.listdir('./queries'):
	print fn
	if os.path.isfile('./queries/'+fn):
        	print 'Running query on file: '+fn
		run_query('./queries/'+fn)
