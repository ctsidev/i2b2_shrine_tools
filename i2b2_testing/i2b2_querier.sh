#! /bin/sh
export I2B2_QUERIER_HOME=.
export WEBCLIENT_URL="ec2-54-200-45-125.us-west-2.compute.amazonaws.com/webclient"
queriesOutput=$I2B2_QUERIER_HOME/run_queries_output.txt
if [ !  -f "$queriesOutput" ] ; then
   touch $queriesOutput
   echo "File $queriesOutput does not exist, now created"
fi

batchDate1=$(date +"%s")
echo >> $queriesOutput
echo "$(date) -- Starting a batch of test queries..." >> $queriesOutput
echo >> $queriesOutput
cd $I2B2_QUERIER_HOME
for file in ./queries/*
do
   queryDate1=$(date +"%s")
   echo
   echo "Filename: $file";
   echo "$file" >> $queriesOutput
   echo $(date)
   echo "$(date)" >> $queriesOutput
   sh curl_command.sh $file > output.txt 
   echo "parsing output file..."
   sh $I2B2_QUERIER_HOME/xml_parse.sh > $I2B2_QUERIER_HOME/outputParsed.txt
   if [ -f "$I2B2_QUERIER_HOME/outputParsed.txt" ] ; then
      cat $I2B2_QUERIER_HOME/outputParsed.txt >> $queriesOutput
      cat $I2B2_QUERIER_HOME/outputParsed.txt
      if [ -f "$I2B2_QUERIER_HOME/outputParsed.txt" ] ; then
         rm $I2B2_QUERIER_HOME/outputParsed_old.txt
      fi
    mv $I2B2_QUERIER_HOME/outputParsed.txt outputParsed_old.txt
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
