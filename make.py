#!/usr/bin/env python3

"""
Generate slides for the presentation.

Usage: ./make.py /path/to/matplotlib/checkout

You must make a clone of the Matplotlib git repository available, and should
have the Carlito and/or Calibri font installed.
"""

import shutil
import subprocess
import sys

from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements, configure_slides
# This must be called before importing other files to make the font available.
check_requirements()  # noqa: F402

from title import create_icon_axes, slides as title_slides
from example import slides as example_slides
from why import slides as why_slides
from general import slides as general_slides
from end import slides as end_slides


METADATA = {
    'Author': 'Elliott Sales de Andrade',
    'Title': 'Slides in Matplotlib — SciPy 2023',
}
MPL_PATH = sys.argv[1]
PAGES = [
    # Tuple of function + any arguments.
    (example_slides, MPL_PATH, ),
    (why_slides, ),
    (general_slides, ),
    (end_slides, ),
]

configure_slides()
with PdfPages('slides.pdf', metadata=METADATA) as pdf:
    # The title page shouldn't have the logo repeated in the top-right corner, so do it
    # first separately.
    title_page = title_slides()
    pdf.savefig(title_page)

    for page, *args in PAGES:
        figs = page(*args)
        if not isinstance(figs, (tuple, list)):
            figs = (figs, )
        for fig in figs:
            create_icon_axes(fig, (0.825, 0.825, 0.2, 0.15),
                             0.3, 0.3, 0.3, [5])
            pdf.savefig(fig)

# Linearize the PDF if qpdf is available.
if shutil.which('qpdf') is not None:
    subprocess.run(['qpdf', 'slides.pdf', '--object-streams=generate',
                    '--linearize', 'scipy2023-lightning-mpl-slide.pdf'])
else:
    shutil.copy('slides.pdf', 'scipy2023-lightning-mpl-slide.pdf')
