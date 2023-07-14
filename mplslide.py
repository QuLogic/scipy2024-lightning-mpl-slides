"""
Common functions for working with slides.
"""

import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager


#: The blue used for Matplotlib logo.
MPL_BLUE = '#11557c'
#: The font to use for the Matplotlib logo.
LOGO_FONT = None
#: A bullet point.
BULLET = '$\N{Bullet}$'
#: The FontProperties to use, Carlito.
FONT = None
#: The size of a slide figure.
FIGSIZE = (19.2, 10.8)
#: The DPI of a slide figure.
DPI = 100


def check_requirements():
    """
    Check requirements to create the slides.

    Currently checks whether the path to a Matplotlib repository is specified,
    and that the Carlito and/or Calibri fonts are available.
    """

    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    # The original font is Calibri, if that is not installed, we fall back
    # to Carlito, which is metrically equivalent.
    calibri = carlito = None
    try:
        matplotlib.font_manager.findfont('Calibri:bold', fallback_to_default=False)
    except ValueError:
        pass
    else:
        calibri = matplotlib.font_manager.FontProperties(family='Calibri',
                                                         weight='bold')
    try:
        matplotlib.font_manager.findfont('Carlito:bold', fallback_to_default=False)
    except ValueError:
        pass
    else:
        carlito = matplotlib.font_manager.FontProperties(family='Carlito',
                                                         weight='bold')
    global FONT, LOGO_FONT
    if calibri is not None:
        LOGO_FONT = calibri
        if carlito is None:
            FONT = calibri
            print('WARNING: Using Calibri for all text. '
                  'Non-logo text may not appear correct.')
        else:
            FONT = carlito
            print('Using Calibri for logo and Carlito for remaining text.')
    elif carlito is not None:
        print('WARNING: Using Carlito for all text. '
              'The logo may not appear correct.')
        LOGO_FONT = carlito
        FONT = carlito
    else:
        sys.exit('Calibri or Carlito font must be installed.')


def configure_slides():
    plt.rcParams['figure.figsize'] = FIGSIZE
    plt.rcParams['figure.dpi'] = DPI

    plt.rcParams['font.family'] = [*FONT.get_family(), 'Segoe UI Emoji']
    plt.rcParams['font.weight'] = FONT.get_weight()
    plt.rcParams['font.size'] = 64
    plt.rcParams['text.color'] = 'tab:grey'

    plt.rcParams['axes.linewidth'] = 3
    plt.rcParams['axes.labelsize'] = 40

    plt.rcParams['xtick.labelsize'] = 32
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['xtick.major.size'] = 7
    plt.rcParams['ytick.labelsize'] = 32
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['ytick.major.size'] = 7

    plt.rcParams['lines.linewidth'] = 3


def slide_heading(fig, text):
    """
    Add a heading to a slide, using a common style.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    text : str
        The text to place in the heading.
    """

    fig.text(0.05, 0.85, text, color='tab:blue', fontproperties=FONT, fontsize=72)
