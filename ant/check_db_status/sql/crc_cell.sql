SELECT TRUNC(CREATE_DATE), count(NAME) FROM QT_QUERY_MASTER WHERE CREATE_DATE > SYSDATE - 365
GROUP BY TRUNC(CREATE_DATE)
ORDER BY TRUNC(CREATE_DATE)