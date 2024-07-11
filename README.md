Plotting Slides in Matplotlib — SciPy 2023 Lightning Talk
=========================================================

This repository contains code to create the presentation for the "Plotting Slides in
Matplotlib" lightning talk at SciPy 2023.

If you want to view the resulting PDF directly, you can [find a generated copy in the
release](https://github.com/QuLogic/scipy2023-lightning-mpl-slides).

Requirements
------------

* Python 3.11+
* NumPy
* Matplotlib >= 3.6.0
* A git checkout of the `matplotlib` source code, to produce the timeline
* The Carlito font
* The OpenMoji Black font

Optionally, you may also make available:

* The font to match the Matplotlib logo, Calibri.
* [`qpdf`](http://qpdf.sourceforge.net/), to linearize the final PDF.

Building
--------

The slides can be created by running:

```bash
$ ./make.py /path/to/matplotlib/checkout
```

which will produce `slides.pdf` directly from Matplotlib and
`scipy2023-lightning-mpl-slides.pdf` as either a copy or a linearized version, depending
on whether `qpdf` is installed.

Overview
--------

Some general setup is contained in `mplslide.py`, namely setting slide size,
picking the font (Calibri and Carlito), and headings and other shortcut
functions. Other styling is mostly consistent, but usually set in the
individual files.

All slides are produced in the remaining Python files.
