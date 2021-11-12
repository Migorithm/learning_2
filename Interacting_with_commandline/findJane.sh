#!/bin/bash

for files in ./*; do
  if [[ "$(basename $files)" =~ "jane_" ]]; then
      echo $(reapath $files) >>oldFiles.txt
  else
      continue
  fi
done
