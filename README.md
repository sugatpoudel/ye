# yenerate

![Python package](https://github.com/groupbool/yenerate/workflows/Python%20package/badge.svg?branch=master)

A simple album art generator for Kanye West's 2018 album *ye*.
This python package uses `pillow` to overlay some text to ye's cover art. This background is a
photograph of the mountains around Kanye's ranch in Wyoming.

The input text is broken into multiple lines so that each line is at most
15 characters long. This package was inspired by [yenerator.com](https://yenerator.com/), which
functions similar to `yenerate` but is entirely client side and written in javascript.

![img](samples/sample_01.jpg)
