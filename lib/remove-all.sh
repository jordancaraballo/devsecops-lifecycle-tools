#!/bin/bash

echo "Removing all specified containers and images ..."

for entry in $INCLUDE; do 
    IMAGE_NAME="$entry"
    
    echo "Removing $REPOSITORY_NAME/$IMAGE_NAME ..."
    docker rmi "$REPOSITORY_NAME/$IMAGE_NAME"
    docker rmi "$IMAGE_NAME"
done

echo "Finished removing all specified containers and images"