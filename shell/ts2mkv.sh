#!/usr/bin/env bash

# Run post processing script on each .ts file

find /Recording /media /media2 -iname '*.ts' -exec /opt/bin/afterglow-post-processing "{}" \;


find . -iname '*.ts' -exec echo "{}" >> /tmp/ts_files.txt \;

find /Recording /media /media2 -iname '*.ts' -printf "%s\n" >> /tmp/ts_sizes.txt;