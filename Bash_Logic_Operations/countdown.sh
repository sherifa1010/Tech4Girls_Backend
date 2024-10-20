#!/bin/bash
#countdown loops

while [[ "$count" -gt 0 ]];
do
   echo "$COUNT"
   COUNT=$((COUNT - 1))
done
    echo "countdown complete!"