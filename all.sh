#!/bin/sh
for i in ${0%/*}/bitmaps/*; do
  echo "${0%/*}/build.sh" "${i##*/}"
done
