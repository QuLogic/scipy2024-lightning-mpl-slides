"""
Slides asking why???
"""

from mplslide import new_slide


def why():
    fig = new_slide()

    fig.text(0.5, 0.5, '🤔 WHY??? 🤔', horizontalalignment='center', fontsize=80)

    return fig


def why_not():
    fig = new_slide()

    fig.text(0.5, 0.5, 'Why Not?', horizontalalignment='center')

    return fig


def slides():
    return (
        why(),
        why_not(),
    )
