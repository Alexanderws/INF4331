
if [ "$#" -gt "1" ]; then
	if [ "$1" == "-a" ]; then
		echo "$2 | $PWD" >> $HOME/.bookmarks
	elif [ "$1" == "-r" ]; then
		echo "REMOVING: $2"
		sed '/$2/d'  $HOME/.bookmarks > $HOME/.bookmarks
		unset $2
	fi
elif [ "$#" -gt "0" ]; then
	echo "Error: Wrong argument format. Supply argument (-a or -r) followed by variable name"
fi
		
 while IFS=" | " read var dest
	do	
	export $var=$dest
done < $HOME/.bookmarks 