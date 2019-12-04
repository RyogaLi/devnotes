#!bin/bash

for i in .; do 
  qsub tar -czf $i.tar.gz $i; 
done
