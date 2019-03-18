if [ $# -gt 0 ]; then
	case $1 in
		sk)
			while sleep 1;
			do
				printf "\033c"
				TZ=Asia/Seoul date 
			done ;;	

		us)
			while sleep 1;
			do
				printf "\033c"
				TZ=America/New_York date
			done ;;	
		no) 
			while sleep 1;
			do
				printf "\033c"
				TZ=Europe/Oslo date  
			done ;;	
	esac
else
	while sleep 1;
	do
		printf "\033c"
		echo `date` 
	done
fi