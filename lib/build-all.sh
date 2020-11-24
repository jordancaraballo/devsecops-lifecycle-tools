#!/bin/bash

SCOPE="all"

if [[ -n $INCLUDE ]]; then 
	SCOPE="specified"
	else INCLUDE="*"
fi

if [[ -n $REPOSITORY_NAME ]]; then 
	echo "Building and tagging $SCOPE XXX images ..."
	else echo "Building $SCOPE XXX images ..."
fi
	
for entry in $INCLUDE; do 
    if [ -d "$PWD/$entry" ]; then
    	cd "$entry"
		
		if [ -f "docker-compose.yml" ]; then
			IMAGE_NAME="$entry"
			
    		docker-compose build "$IMAGE_NAME"
    		
			if [[ -n $REPOSITORY_NAME ]]; then 
				echo "Tagging $IMAGE_NAME for repository $REPOSITORY_NAME ..."
				docker tag "$IMAGE_NAME" "$REPOSITORY_NAME/$IMAGE_NAME"
			fi
		fi    	
    	
    	cd ..
    fi
done

if [[ -n $REPOSITORY_NAME ]]; then 
	echo "Finished building and tagging $SCOPE django images ..."
	else echo "Finished building $SCOPE XXX images ..."
fi

