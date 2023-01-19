import urllib.request
import re, os, sys

def optimise_png(data):
  import oxipng
  data = oxipng.optimize_from_memory(
    data,
    level = 6,
    interlace = oxipng.Interlacing.Off,
    strip = oxipng.Headers.all(),
    optimize_alpha = True,
    bit_depth_reduction = False,
    color_type_reduction = False)

def download_emojis(url, dir, force = False):
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')]

  with opener.open(url) as f:
    lines = f.read().decode('utf-8').splitlines()

  sk = re.compile('^.*srcset=.*?/thumbs/\d+/[\w\d_-]+/\d+/.*?\.png')
  ue = re.compile('^.*? (data-|)srcset=\"([^ ]+) ')
  tu = re.compile('/thumbs/\d+/')
  lines = filter(lambda line: sk.match(line), lines)
  for line in lines:
    m = ue.match(line)
    url = tu.sub('/thumbs/160/', m.group(2)) # 72, 144, 160, 240, 320
    file = os.path.basename(url)
    path = os.path.join(dir, file)
    if os.path.exists(path):
      if not force:
        print('Skipped %s' % file)
        continue
    with opener.open(url) as f:
      data = f.read()
    data = optimise_png(data)
    with open(path, 'wb') as f:
      f.write(data)
    print('Saved %s' % file)

def main(argv):
  if len(argv) < 3:
    print('emoji_saver.py URL BMPDIR', file = sys.stderr)
    sys.exit(1)
  url = argv[1]
  dir = os.path.realpath(argv[2])
  download_emojis(url, dir)

if __name__ == '__main__':
  main(sys.argv)
