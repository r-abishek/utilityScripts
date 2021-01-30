#!/bin/bash
find . -type f -exec dirname {} + | uniq -c | while read n d;do echo "Directory:$d Files:$n Moving first:$(($n / 10))";mkdir q-p ../maindir2${d:1};find $d -type f | head -n $(($n / 10)) | while read file;do mv $file ../maindir2${d:1}/;done;done

