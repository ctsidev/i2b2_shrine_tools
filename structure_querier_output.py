import sys
import re

filename =  sys.argv[1]

with open(filename,"r") as oFile:
   data=oFile.read()

query_result_matcher=re.compile(r"(\.\/.+?\.)\n\n", re.DOTALL)

print "query|execution date-time|mins|secs|UCD|UCI|UCLA|UCSD|UCSF"
data

for query_match in query_result_matcher.finditer(data):
   query_result  = query_match.groups()
   mins = "0"
   secs = "0"
   if "seconds elapsed" in query_result[0]:
      result1 = query_result[0].split('\n')
      elapsedtime = result1[len(result1) - 1].split()
      if len(elapsedtime) >= 3:
         mins = elapsedtime[0]
         secs = elapsedtime[3]
   query_parts_matcher = re.compile(r"(.+?)\n",re.DOTALL)
   query_result_csv = ""
   comma = ""
   colnum = 0
   ucd = ""
   uci = ""
   ucla = ""
   ucsd = ""
   ucsf = ""
   query_result_csv0 = ''
   for query_part_match in query_parts_matcher.finditer(query_result[0]):
      query_part = query_part_match.groups()
      query_result_csv +=  comma +  query_part[0]
      comma = "|"
      if colnum == 1:
         query_result_csv += "|" + mins + "|" + secs
         query_result_csv0 = query_result_csv
      #print "query results after mins sec %s" % query_result_csv
      if colnum > 1:
         #print "query_part %s" % query_part[0]
         array1 = query_part[0].split(":")
         school = array1[0]
         count = ''
         status = ''
         results = ''
         if len(array1) > 1:
            results = array1[1]
            array2 = array1[1].split(",")
            count = array2[0]
            if len(array2) > 1:
               status = array2[1]
         #print "UC school %s" % school
         #print "results %s" % results
         #print "data count %s" % count
         #print "query status %s" % status
         if school == 'UCD':
            if status == 'ERROR' or status == 'QUEUED':
               ucd = status
            elif count != '0' and count != '-1':
               ucd = count
            else: ucd = results
         elif school == 'UCI':
            if status == 'ERROR' or status == 'QUEUED':
               uci = status
            elif count != '0' and count != '-1': 
               uci = count
            else: uci = results
         elif school == 'UCLA':
            if status == 'ERROR' or status == 'QUEUED':
               ucla = status
            elif  count != '0' and count != '-1':
               ucla = count
            else: ucla = results
         elif school == 'UCSD':
            if status == 'ERROR' or status == 'QUEUED':
               ucsd = status
            elif count != '0' and count != '-1':
               ucsd = count
            else: ucsd = results
         elif school == 'UCSF':
            if status == 'ERROR' or status == 'QUEUED':
               ucsf = status
            elif count != '0' and count != '-1': 
               ucsf = count
            else: ucsf = results
      #print "UCD %s UCI %s UCLA %s UCSD %s UCSF %s " % (ucd, uci, ucla, ucsd, ucsf)
      colnum = colnum + 1
   query_result_csv0 += "|" + ucd + "|" + uci + "|" + ucla + "|" + ucsd + "|" + ucsf
   print query_result_csv0

