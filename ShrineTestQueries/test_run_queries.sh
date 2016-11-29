#! /bin/sh
#export UCREX_QUERIER_HOME=~/scripts/ucrexprod_querier
export UCREX_QUERIER_HOME=/home/snchau/scripts/ucrexprod_querier
queriesOutput=$UCREX_QUERIER_HOME/run_queries_output.txt
if [ !  -f "$queriesOutput" ] ; then
   touch $queriesOutput
   echo "File $queriesOutput does not exist, now created"
fi

batchDate1=$(date +"%s")
echo >> $queriesOutput
echo "$(date) -- Starting a batch of test queries..." >> $queriesOutput
echo >> $queriesOutput
cd $UCREX_QUERIER_HOME
for file in ./queries/*
do
   queryDate1=$(date +"%s")
   echo 
   echo $file;
   echo "$file" >> $queriesOutput
   echo $(date)
   echo "$(date)" >> $queriesOutput
   sh $UCREX_QUERIER_HOME/curl_command.sh $file > $UCREX_QUERIER_HOME/output.txt ; sh $UCREX_QUERIER_HOME/xml_parse.sh > $UCREX_QUERIER_HOME/outputParsed.txt
   if [ -f "$UCREX_QUERIER_HOME/outputParsed.txt" ] ; then
      cat $UCREX_QUERIER_HOME/outputParsed.txt >> $queriesOutput
      cat $UCREX_QUERIER_HOME/outputParsed.txt
      if [ -f "$UCREX_QUERIER_HOME/outputParsed.txt" ] ; then
         rm $UCREX_QUERIER_HOME/outputParsed_old.txt
      fi  
    mv $UCREX_QUERIER_HOME/outputParsed.txt outputParsed_old.txt
    fi
    queryDate2=$(date +"%s")
    queryDiff=$(($queryDate2-$queryDate1))
    elapsedQtime="$(($queryDiff / 60)) minutes and $(($queryDiff % 60)) seconds elapsed for query $file."
   echo $elapsedQtime
   echo $elapsedQtime >> $queriesOutput
   echo >> $queriesOutput
done
batchDate2=$(date +"%s")
batchDiff=$(($batchDate2-$batchDate1))
batchElapsedTime="$(($batchDiff / 60)) minutes and $(($batchDiff % 60)) seconds elapsed for batch."
echo
echo $batchElapsedTime
echo >> $queriesOutput
echo "$(date) -- Batch ended.  $batchElapsedTime" >> $queriesOutput
echo >> $queriesOutput
echo "*********************************************************************" >> $queriesOutput
