#!/bin/bash

for file in $(ls -1); do echo $file; filename="${file%.*}"; extension="${file##*.}"; i="_4."; cp $file $filename$i$extension; done
