"""
Slides asking why???
"""

import matplotlib.pyplot as plt


def why():
    fig = plt.figure()

    fig.text(0.5, 0.5, '🤔 WHY??? 🤔', horizontalalignment='center', fontsize=80)

    return fig


def why_not():
    fig = plt.figure()

    fig.text(0.5, 0.5, 'Why Not?', horizontalalignment='center')

    return fig


def slides():
    return (
        why(),
        why_not(),
    )
