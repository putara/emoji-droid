# WhatsThis

Generate an emoji font with the images from [Emojipedia](https://emojipedia.org/).

## Prerequisties

- Python 3.x

## HowToBuild

1. Install requirements
    ```
    pip install -r requirements.txt
    ```
2. Download images
    ```
    python emoji_saver.py [URL] ./bitmaps/foo
    ```
2. Build
    ```
    ./build.sh foo
    ```
3. Copy `./output/foo-emoji.ttf` into a mobile device
4. Use a font replacement app, or a Magisk module like [this one](https://github.com/nongthaihoang/custom_font_installer), to override the system emoji font

## Acknowledge

- Portion of code has been taken from [noto-emoji](https://github.com/googlefonts/noto-emoji/) and [color_emoji](https://github.com/googlefonts/noto-emoji/tree/main/third_party/color_emoji), both of which are released under the Apache License 2.0

## License

Read [this page](https://emojipedia.org/licensing/).
**Do not distribute any generated fonts.**
