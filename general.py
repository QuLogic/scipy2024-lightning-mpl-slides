"""
Slides showing minimal setup for slides.
"""

from matplotlib import cbook, pyplot as plt
import numpy as np

from mplslide import slide_heading

CODE = dict(font='monospace', fontsize=48, verticalalignment='top')


def page1():
    fig = plt.figure()
    slide_heading(fig, 'Slide setup')

    fig.text(0.05, 0.75, 'Set a big figure (1080p):')
    fig.text(0.05, 0.7, """\
plt.rcParams["figure.figsize"] = (
    19.2, 10.8)
plt.rcParams["figure.dpi"] = 100
""",
             **CODE)

    return fig


def page2():
    fig = plt.figure()
    slide_heading(fig, 'Slide setup')

    fig.text(0.05, 0.75, 'Set a nice font:')
    fig.text(0.05, 0.7, """\
plt.rcParams['font.family'] = [
    'Carlito',
    'OpenMoji Black',
]
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.size'] = 64
plt.rcParams['text.color'] = 'tab:grey'
""",
             **CODE)

    return fig


def page3():
    fig = plt.figure()
    slide_heading(fig, 'Slide setup')

    fig.text(0.05, 0.75, 'Set better Axes sizes:')
    fig.text(0.05, 0.7, """\
plt.rcParams['axes.linewidth'] = 3
plt.rcParams['axes.labelsize'] = 40
plt.rcParams['xtick.labelsize'] = 32
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['xtick.major.size'] = 7
plt.rcParams['ytick.labelsize'] = 32
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 7
plt.rcParams['lines.linewidth'] = 3
""",
             **CODE)

    return fig


def page4():
    fig = plt.figure()
    slide_heading(fig, 'Save the slides')

    fig.text(0.05, 0.8, """\
from matplotlib.backends.backend_pdf import (
    PdfPages)

figures = [...]
with PdfPages('name.pdf') as pdf:
    for fig in figures:
        add_logo(fig)
        pdf.savefig(fig)
""",
             **CODE)

    return fig


def page5():
    fig = plt.figure()
    slide_heading(fig, 'Add a slide title')

    fig.text(0.05, 0.8, '''\
def slide_heading(fig, text):
    """
    Add a heading to a slide,
    using a common style.
    """

    fig.text(0.05, 0.85, text,
             color='tab:blue', fontsize=72)
''',
             **CODE)

    return fig


def page6():
    fig = plt.figure()
    slide_heading(fig, 'Add a plot')

    fig.text(0.05, 0.8, '''\
fig, ax = plt.subplots()
slide_heading(fig, 'Add a plot')
ax.plot(np.sin(np.linspace(0, 5*np.pi, 100)))
''',
             **CODE)

    ax = fig.add_subplot([0.1, 0.1, 0.8, 0.5])
    ax.plot(np.sin(np.linspace(0, 5*np.pi, 100)))

    return fig


def page7():
    fig = plt.figure()
    slide_heading(fig, 'Write some text')

    fig.text(0.05, 0.75, 'Here is some explanatory text')
    fig.text(0.05, 0.7, """\
fig.text(0.05, 0.75,
         'Here is some explanatory text')
""",
             **CODE)

    return fig


def page8():
    fig = plt.figure()
    slide_heading(fig, 'Add an image')

    fig.text(0.05, 0.8, '''\
img = plt.imread('grace_hopper.jpg')
fig.figimage(img, xo=..., yo=...)
''',
             **CODE)

    img = plt.imread(cbook.get_sample_data('grace_hopper.jpg'))
    fig.figimage(img, xo=(1920 - img.shape[1]) / 2, yo=30)

    return fig


def slides():
    return (
        page1(),
        page2(),
        page3(),
        page4(),
        page5(),
        page6(),
        page7(),
        page8(),
    )
