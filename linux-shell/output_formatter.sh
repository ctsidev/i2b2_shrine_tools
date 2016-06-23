#! /bin/sh
cat run_queries_output.txt | sed 's/\(Mon\|Tue\|Wed\|Thu\|Fri\|Sat\|Sun\)/<\/res><res><timestamp>\1/g'|sed 's/2015/2015<\/timestamp>/g'|sed 's/\(UCLA\|UCSD\|UCSF\|UCI\|UCD\) SHRINE:\(.*\)/<site>\1:\2<\/site>/g'|sed 's/\([0-9]*\.[0-9]*\)/<time> \1<\/time>/g'|grep -Ev 'DOCTYPE|body|Tomcat|pdesai|elapsed|\^' > test.txt; sed -i '1s/^<\/res>/<responses>/' test.txt; echo "</res></responses>" >> test.txt
