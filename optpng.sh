#!/usr/bin/sh
if [ -z $1 ]; then
  echo './optpng.sh DIRNAME'
  exit 1
fi
if ! which oxipng >/dev/null 2>&1; then
  echo 'oxipng is not installed'
fi
files=()
for i in ${0%/*}/bitmaps/$1/*.png; do
  files+=("$i")
done
oxipng -a -omax -i0 --strip all --nc --nb "${files[@]}"
