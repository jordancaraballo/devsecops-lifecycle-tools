#!/bin/bash

if [[ -z $REPOSITORY_NAME ]]; then
	export REPOSITORY_NAME="XXX"
fi

if [[ -n $REPOSITORY_NAME ]]; then 

	SCOPE="all"

	if [[ -n $INCLUDE ]]; then 
		SCOPE="specified"
	fi

	echo "Pushing $SCOPE Docker images to $REPOSITORY_NAME ...";
	
	if [ "$SCOPE" = "all" ]; then
		for entry in *; do 
		
			if [ -d "$entry" ]; then
				if [ -f "$entry/docker-compose.yml" ]; then		
					IMAGE_NAME="$entry"
			
					echo "Pushing $REPOSITORY_NAME/$IMAGE_NAME ..."
					docker push "$REPOSITORY_NAME/$IMAGE_NAME"
				fi    	
			fi
		done
	else
		for entry in $INCLUDE; do 
			IMAGE_NAME="$entry"
			
			echo "Pushing $REPOSITORY_NAME/$IMAGE_NAME ..."
			docker push "$REPOSITORY_NAME/$IMAGE_NAME"
		done
	fi

	echo "Finished pushing $SCOPE Docker images to $REPOSITORY_NAME"
fi
	
