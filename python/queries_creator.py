from i2b2_query_xml_generate import generate_i2b2_query
import csv

def generate_queries_all_years(username,password,query_name,item_name,path,tooltip):
        for year in range(2006, 2017):
		year_s = str(year)
                date_from=year_s+'-01-01T00:00:00.000-05:00'
                date_to=year_s+'-12-31T00:00:00.000-05:00'
                shrine_redirect_url='http://URL:PORT/shrine/rest/i2b2/request'
                i2b2_domain='i2b2demo'
                query_xml = generate_i2b2_query(i2b2_domain,username,password,query_name,item_name,
                	path,tooltip,date_from,date_to,shrine_redirect_url)
                fd = open('queries/'+year_s+'_'+query_name+'.xml','w')
                fd.write(query_xml)
                fd.close()

with open('data/input.csv','rb') as csvfile:
	q_reader = csv.DictReader(csvfile,delimiter=',')
	for row in q_reader:
		username = 'USERNAME'
		password = 'PASSWORD'
		path = row['ontology_path']
		tooltip = row['tooltip']
		row_num = row['row_num']
		query_name = row_num
		item_name='Asthma'
		generate_queries_all_years(username,password,query_name,item_name,path,tooltip)

