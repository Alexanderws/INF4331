if [ $# -lt 2 ]; then
	echo "Error: Invalid arguments. Use a command (P, S, M or m) followed by numbers."
	exit
fi

option=0

case $1 in
	S)
		option=S
		shift; ;;
	P) 
		option=P
		shift; ;;
	M) 
		option=M
		shift; ;;
	m) 
		option=m
		shift; ;;
esac

if [ "$option" != "0" ]; then
	let x=$1 
		shift;
		while [ $# -gt 0 ]  
		do	
			if [ "$option" == "S" ]; then
				let x=x+$1
			fi
			if [ "$option" == "P" ]; then
				let x=x*$1
			fi
			if [ "$option" == "M" ]; then
				if [ $1 -gt $x ]; then
					let x=$1
				fi
			fi
			if [ "$option" == "m" ]; then
				if [ $1 -lt $x ]; then
					let x=$1
				fi
			fi
			shift;
		done
		echo $x
fi