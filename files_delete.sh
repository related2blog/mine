#!/bin/bash

#this script is useful if you have to delete same files again and again during your testing
# Fill files to be deleted within quotes below
LIST_OF_FILES=(
				'/tmp/ddd'
				'/tmp/sssss'	

				)
				
if [ $EUID -ne 0 ];
        then
        echo "You must run this script as root"
        exit 

fi


cleanup()
{
	file=$1
	if [ -f $file ];
		then
		rm -rf $file
		if [ $? -eq 0 ];
		then
			echo "$file is deleted"
		elif [ $? -ne 0 ];
		then
			echo "FAILED to delete $file !!!"
		fi
	else
		echo "$file --> NOT THERE !!!"
	fi
}


for i in ${LIST_OF_FILES[*]};
do
	cleanup $i
done
