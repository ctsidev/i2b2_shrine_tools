The purpose of the scripts included in this folder is to execute certain SHRINE queries to check for issues, e.g.:
  - whether all nodes on this SHRINE network (e.g. UCReX) are responding to the queries by returning non-zero results
  - whether a query times out
  - to get indications of data/ontology issues
  
This process requires a user account to log in to the local shrine web client and access to a linux serverto run the scripts below.

A subfolder named 'queries' needs to be created at the level where these scripts reside.  Each test scriptmust be generated as XML file and stored in this 'queries' folder.  The steps to generate these XML files areoutlined below.

SCRIPTS:
test_run_queries.sh     This is the main script, crontab schedulable, that iterates through the ./queries/ subfolder and                                         and invokes the curl_command.sh and xml_parse.sh scripts to execute the shrine/i2b2 queries stored under                                the 'queries' subfolder.  The results and query elapsed time of the queries are appended to the                                        run_queries_output.txt file.  To schedule the queries (all queries under the 'queries' subfolder) to
                        run at specific time/day (e.g. run once in the morning, once in the evening), schedule this script
                        via crontab.      

curl_command.sh         This script contains the URL used by 'curl' to log on to the designated shrine network  (e.g. UCReX)                            via the local shrine webclient.  It needs to be modified to match the URL of the local site's                                           shrine webclient. The script does a curl "POST" of the test query XML file.      

xml_parse.sh            This script executes the 'xmlstarlet' command line tool to edit the XML output and parse the results, 
                        one line for each SHRINE node.      

stucture_querier_output.py   This Python script takes the 'run_queries_output.txt' file and formats the contents into                         a pipe-delimited output file. Customization not required if the SHRINE network is UCReX.                                                To execute this script:                     
                             python structure_querier_output.py run_queries_output.txt > testQueryOutFile.txt 
                        the output file 'testQueryOutFile.txt' will have this heading:  
                                     query|execution date-time|mins|secs|UCD|UCI|UCLA|UCSD|UCSF                              
                        It can be imported into Excel for viewing.
                        
                        
TEST QUERY XML file creation:
1) Open a browser and log on to the local shrine webclient
2) Build the query (e.g. 'asthma', age '0-9 years old') you want to run using the web client  
3) Click Run Query -> OK 
4) When the results appear in the Query Status box, click on 'Message Log', scroll down to find 'runQueryInstance_fromQueryDefinition', click on it to display its contents.  
5) Copy all the lines next to the pink vertical bar.    
6) Back on the server, 'cd' to the 'queries' folder, open the 'vi' editor (e.g. vi asthmaAge0-9.txt), then insert the text copied in step 5
7) In the <security> section, edit the 'username' (if change is needed) and '<password>'.  The <password>line should reflect this (where myPassword is the one associated with the 'username'):           <password>myPassword</password>  
8) Save the file.
9) On the shrine web client, click on 'Clear' and close the 'Message Log' window
10) Repeat steps 2-9 for additional queries 
