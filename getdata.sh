#!/bin/bash

for year in {2012..2014}
do
  if [ ! -e nvdcve-2.0-${year}.xml ]; then
    wget https://nvd.nist.gov/static/feeds/xml/cve/nvdcve-2.0-${year}.xml
  fi
done
