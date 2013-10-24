#! /bin/bash

#single IP proxy script - accepts 2 arguments, IP and Port

	curl -vvv -x https://$1:$2 https://ctf.fluxfingers.net/ref/MyHl7CtvFtdqnfX &

