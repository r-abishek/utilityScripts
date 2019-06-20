git ls-files > ~/listOfFiles
cat ~/listOfFiles | xargs wc -l
rm -rvf ~/listOfFiles
