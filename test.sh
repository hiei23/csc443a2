#!/bin/bash

INPUT_FILES=(
	"books.json" 
	"records.json" 
	"friends.json" 
	"dna.json"
	)

FILES=(
	"inverted_index" 
	"join" 
	"friend_count" 
	"unique_trims"
	)

# get length of an array
arraylength=${#INPUT_FILES[@]}

mkdir results difference

printf "\n>>>>>>>>>>>>> Testing Files <<<<<<<<<<<<<\n\n"

for (( i=1; i < ${arraylength} + 1; i++ ));
do
  	echo "Testing: ${FILES[$i-1]}" 
  	python "${FILES[$i-1]}.py" "input/${INPUT_FILES[$i-1]}" > "results/${FILES[$i-1]}.json"
  
  	printf "\n>>>>>>>>>>>>> Checking Difference <<<<<<<<<<<<<\n\n"
  	diff "solutions/${FILES[$i-1]}.json" "results/${FILES[$i-1]}.json" > "difference/${FILES[$i-1]}_diff.txt"
done