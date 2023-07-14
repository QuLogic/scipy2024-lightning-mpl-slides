"""
A timeline of releases.

This file is based on `examples/lines_bars_and_markers/timeline.py` in the
Matplotlib repository.
"""

from datetime import datetime
import subprocess

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from title import create_icon_axes
from mplslide import slide_heading


def logo():
    fig = plt.figure()
    slide_heading(fig, 'Example: Logo')

    create_icon_axes(fig, (0.05, 0.05, 0.9, 0.7),
                     3, 3, 3, [1, 3, 5, 7])
    return fig


def timeline(mpl_path):
    """
    Create slide for release history.

    Parameters
    ----------
    mpl_path : str or pathlib.Path
        Path to the Matplotlib checkout used to find release tags and dates.
    """
    fig = plt.figure()

    slide_heading(fig, 'Example: Release History')

    tags = subprocess.run(['git', 'tag', '-l',
                           '--format=%(refname:strip=2) %(creatordate:short)'],
                          cwd=mpl_path, capture_output=True, text=True)
    dates = []
    names = []
    for item in tags.stdout.splitlines():
        tag_name, date = item.split(' ', 1)
        if 'rc' not in tag_name and 'b' not in tag_name:
            dates.append(datetime.fromisoformat(date))
            names.append(tag_name)

    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    ax = fig.add_axes((0.05, 0.11, 0.9, 0.7))

    ax.vlines(dates, 0, levels, color="tab:red", linewidth=3)
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w", linewidth=3, markersize=10)

    # Annotate lines.
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top",
                    fontsize=24)

    # Format xaxis with 4 month intervals.
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=24)

    # Remove y axis and spines.
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y=0.1)

    this_scipy = datetime(2023, 7, 12)
    last_scipy = datetime(2022, 7, 13)

    # Annotate range between last SciPy and this SciPy.
    ax.axvspan(last_scipy, this_scipy, alpha=0.5)

    # Only plot the last 5 years before this SciPy.
    ax.set_xlim(this_scipy.replace(year=this_scipy.year - 5), this_scipy)

    return fig


def section_text():
    fig = plt.figure()
    slide_heading(fig, 'Examples')

    fig.text(0.05, 0.7, 'Both are examples from Matplotlib gallery')

    for i, link in enumerate([
        'https://matplotlib.org/stable/gallery/misc/logos2.html',
        'https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html',
    ]):
        t = fig.text(0.05, 0.5 - 0.15*i, link, fontsize=40)
        t.set_url(link)

    return fig


def slides(mpl_path):
    return (
        logo(),
        timeline(mpl_path),
        section_text(),
    )
