xmlstarlet sel -t -m "//query_result_instance" -v "concat(description,':',set_size,',',query_status_type/name)" -n $UCREX_QUERIER_HOME/output.txt

