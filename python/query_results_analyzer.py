import os
import xml.etree.ElementTree
from datetime import datetime

def readFile(filename):
	with open(filename, 'r') as resultfile:
		resultData = resultfile.read()
		analyzeResultXml(filename,resultData)

def analyzeResultXml(filename,resultXml):
	e = xml.etree.ElementTree.fromstring(resultXml)
	filenameparts =  filename.split('/')[3]
	query_number = filenameparts.split('_')[1].split('.')[0]
	query_year = filenameparts.split('_')[0]
	result = query_number+","+query_year+","
	errors = ""
	uclaResult = "ERROR,0,"
        ucsfResult = "ERROR,0,"
        uciResult = "ERROR,0,"
 	ucsdResult = "ERROR,0,"
        ucdResult = "ERROR,0,"
	for atype in e.findall('.//query_result_instance'):
    		siteName=atype.find('description').text
		siteStatus=atype.find('query_status_type').find('name').text
		sitePatientCount=atype.find('set_size').text

		if(siteStatus=='FINISHED'):
			startTimeString = atype.find('start_date').text
			endTimeString = atype.find('end_date').text
			startTime = datetime.strptime(startTimeString, '%Y-%m-%dT%H:%M:%S.%f-07:00')
			endTime = datetime.strptime(endTimeString, '%Y-%m-%dT%H:%M:%S.%f-07:00')
			timeTaken = (endTime - startTime).seconds
			currentResult = (sitePatientCount + ",{0},").format(timeTaken)
			if siteName=="UCLA":
				uclaResult = currentResult
			elif siteName== "UCSF":
				ucsfResult = currentResult
			elif siteName=="UCI":
                                uciResult = currentResult
			elif siteName=="UCSD":
                                ucsdResult = currentResult
			elif siteName=="UCD":
                                ucdResult = currentResult	

		else:
			siteError=atype.find('query_status_type').find('description').text
			errors+=siteName+","+siteError

	result += uclaResult + ucsfResult + uciResult + ucsdResult + ucdResult

	result+="\n"
	errors+="\n"
	fd = open('results.csv','a')
	fd.write(result)
	fd.close()
	fd_e = open('errors.csv','a')
	fd_e.write(errors)
	fd_e.close()

for fn in os.listdir('./results/queries'):
        if os.path.isfile('./results/queries/'+fn):
                readFile('./results/queries/'+fn)
