#!/usr/bin/env bash

# Run post processing script on each .ts file

find . -iname '*.ts' -exec /opt/bin/post-processing.sh "{}" \;


find . -iname '*.ts' -exec echo "{}" >> /tmp/ts_files.txt \;