#!/bin/sh
if [ -z $1 ]; then
  echo './build.sh DIRNAME'
  exit 1
fi

INFILE=./base.ttx.tmpl
BMPDIR=./bitmaps

TMPFILE=./output/$1-temp.ttx
TMPFONT=./output/$1-temp.ttf
OUTFONT=./output/$1-emoji.ttf
EMOJIDIR=$BMPDIR/$1

rm -f $TMPFILE $TMPFONT $OUTFONT >/dev/null 2>&1
set +e
# python ./emoji_saver.py $EMOJIDIR
python ./gen_ttx.py $INFILE $TMPFILE $EMOJIDIR
fonttools ttx $TMPFILE
python ./color_emoji/emoji_builder.py $TMPFONT $OUTFONT $EMOJIDIR
