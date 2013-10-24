#! /bin/bash
#proxyscript.sh ($1) 
#first argument should be file name, with proxy values listed as x.x.x.x:xx

cat $1 |while read line;do

	curl -vvv -x http://$line https://ctf.fluxfingers.net/ref/MyHl7CtvFtdqnfX &

done  
