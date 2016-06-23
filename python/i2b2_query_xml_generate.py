from xml.etree.ElementTree import Element, SubElement, Comment, tostring

def generate_i2b2_query(i2b2_domain,shrine_username,shrine_password,q_name,query_ontology_name, 
	query_ontology_path,query_ontology_tooltip,date_from,date_to,shrine_redirect_url):
	ns6_request = Element('ns6:request')

	comment = Comment('I2B2 query generated using python')
	ns6_request.append(comment)

	message_header =  SubElement(ns6_request, 'message_header')
	proxy =  SubElement(message_header, 'proxy')
	redirect_url =  SubElement(proxy, 'redirect_url')
	redirect_url.text=shrine_redirect_url
	sending_application =  SubElement(message_header, 'sending_application')
	application_name =  SubElement(sending_application, 'application_name')
	application_name.text='i2b2_QueryTool'
	application_version =  SubElement(sending_application, 'application_version')
	application_version.text='1.6'
	sending_facility =  SubElement(message_header, 'sending_facility')
	facility_name =  SubElement(sending_facility, 'facility_name')
	facility_name.text='PHS'
	receiving_application =  SubElement(message_header, 'receiving_application')
	application_name =  SubElement(receiving_application, 'application_name')
	application_name.text='i2b2_DataRepositoryCell'
	application_version =  SubElement(receiving_application, 'application_version')
	application_version.text='1.6'
	receiving_facility =  SubElement(message_header, 'receiving_facility')
	facility_name =  SubElement(receiving_facility, 'facility_name')
	facility_name.text='PHS'
	security =  SubElement(message_header, 'security')
	domain =  SubElement(security, 'domain')
	domain.text=i2b2_doman
	username =  SubElement(security, 'username')
	username.text=shrine_username
	password =  SubElement(security, 'password')
	password.text=shrine_password
	message_type =  SubElement(message_header, 'message_type')
	message_code =  SubElement(message_type, 'message_code')
	message_code.text='Q04'
	event_type =  SubElement(message_type, 'event_type')
	event_type.text='EQQ'
	message_control_id =  SubElement(message_header, 'message_control_id')
	message_num =  SubElement(message_control_id, 'message_num')
	message_num.text='8v1K623mDIbPtJ8rO3FMy'
	instance_num =  SubElement(message_control_id, 'instance_num')
	instance_num.text='0'
	processing_id_parent =  SubElement(message_header, 'processing_id')
	processing_id =  SubElement(processing_id_parent, 'processing_id')
	processing_id.text='P'
	processing_mode =  SubElement(processing_id_parent, 'processing_mode')
	processing_mode.text='I'
	accept_acknowledgement_type =  SubElement(message_header, 'accept_acknowledgement_type')
	accept_acknowledgement_type.text='messageId'
	project_id =  SubElement(message_header, 'project_id')
	project_id.text='SHRINE'

	request_header =  SubElement(ns6_request, 'request_header')
	result_waittime_ms =  SubElement(request_header, 'result_waittime_ms')
	result_waittime_ms.text='180000'

	message_body =  SubElement(ns6_request, 'message_body')
	ns4_psmheader =  SubElement(message_body, 'ns4:psmheader')
	user =  SubElement(ns4_psmheader, 'user')
	user.text='shrine'
	patient_set_limit =  SubElement(ns4_psmheader, 'patient_set_limit')
	patient_set_limit.text='0'
	estimated_time =  SubElement(ns4_psmheader, 'estimated_time')
	estimated_time.text='0'
	query_mode =  SubElement(ns4_psmheader, 'query_mode')
	query_mode.text='optimize_without_temp_table'
	request_type =  SubElement(ns4_psmheader, 'request_type')
	request_type.text='CRC_QRY_runQueryInstance_fromQueryDefinition'

	ns4_request =  SubElement(message_body, 'ns4:request')
	query_definition =  SubElement(ns4_request, 'query_definition')
	query_name =  SubElement(query_definition, 'query_name')
	#query_name.text='Asthma(493)@testtime'
	query_name.text = 'DashboardQuery'+q_name
	query_timing =  SubElement(query_definition, 'query_timing')
	query_timing.text='ANY'
	specificity_scale =  SubElement(query_definition, 'specificity_scale')
	specificity_scale.text='0'
	panel =  SubElement(query_definition, 'panel')
	panel_number =  SubElement(panel, 'panel_number')
	panel_number.text='1'
	panel_date_from = SubElement(panel, 'panel_date_from')
        panel_date_from.text = date_from
        panel_date_to  = SubElement(panel, 'panel_date_to')
        panel_date_to.text = date_to
	panel_accuracy_scale =  SubElement(panel, 'panel_accuracy_scale')
	panel_accuracy_scale.text='100'
	invert =  SubElement(panel, 'invert')
	invert.text='0'
	panel_timing =  SubElement(panel, 'panel_timing')
	panel_timing.text='ANY'
	total_item_occurrences =  SubElement(panel, 'total_item_occurrences')
	total_item_occurrences.text='1'
	item =  SubElement(panel, 'item')
	hlevel =  SubElement(item, 'hlevel')
	hlevel.text='5'
	item_name =  SubElement(item, 'item_name')
	item_name.text = query_ontology_name
	item_key =  SubElement(item, 'item_key')
	item_key.text = query_ontology_path
	tooltip =  SubElement(item, 'tooltip')
	tooltip.text = query_ontology_tooltip
	class_item =  SubElement(item, 'class')
	class_item.text='ENC'
	item_icon =  SubElement(item, 'item_icon')
	item_icon.text='FA'
	item_is_synonym =  SubElement(item, 'item_is_synonym')
	item_is_synonym.text='false'
	result_output_list =  SubElement(ns4_request, 'result_output_list')
	result_output =  SubElement(result_output_list, 'result_output')
	return tostring(ns6_request)
