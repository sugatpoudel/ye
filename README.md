# yenerate

![Python package](https://github.com/groupbool/yenerate/workflows/Python%20package/badge.svg?branch=master)

A simple album art generator for Kanye West's 2018 album *ye*.
This python package uses `pillow` to overlay some text to ye's cover art. This background is a
photograph of the mountains around Kanye's ranch in Wyoming.

The input text is broken into multiple lines so that each line is at most
15 characters long. This package was inspired by [yenerator.com](https://yenerator.com/), which
functions similar to `yenerate` but is entirely client side and written in javascript.

![img](samples/sample_01.jpg)

## Usage

`yenerate` requires python 3 to function properly. Download a `.whl` release from
this repository's [releases](https://github.com/groupbool/yenerate/releases). You can
use pip to directly install `yenerate` from this file.

```
pip install <yenerate-release>.whl
yenerate "I hate being Bi-Polar it's awesome"
```