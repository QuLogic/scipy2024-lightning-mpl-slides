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
from mplslide import add_qrcode, slide_heading


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
    releases = []
    for item in tags.stdout.splitlines():
        tag_name, date = item.split(' ', 1)
        if 'rc' not in tag_name and 'b' not in tag_name:
            dates.append(datetime.fromisoformat(date))
            releases.append(tag_name.lstrip('v'))
    releases = [
        tuple(release.split('.'))  # Split into components.
        for release in releases
    ]
    dates, releases = zip(*sorted(zip(dates, releases)))  # Sort by increasing date.

    def is_feature(release):
        return release[-1] == '0'

    # Choose some nice levels: alternate meso releases between top and bottom, and
    # progressively shorten the stems for micro releases.
    levels = []
    major_meso_releases = sorted({release[:2] for release in releases})
    for release in releases:
        major_meso = release[:2]
        micro = int(release[2])
        h = 1 + 0.8 * (5 - micro)
        level = h if major_meso_releases.index(major_meso) % 2 == 0 else -h
        levels.append(level)

    ax = fig.add_axes((0.05, 0.11, 0.9, 0.7))

    # The vertical stems.
    ax.vlines(dates, 0, levels, linewidth=3,
              color=[('tab:red', 1 if is_feature(release) else .5)
                     for release in releases])
    # The baseline.
    ax.axhline(0, color="black", linewidth=3)
    # The markers on the baseline.
    meso_dates = [date for date, release in zip(dates, releases)
                  if is_feature(release)]
    micro_dates = [date for date, release in zip(dates, releases)
                   if not is_feature(release)]
    ax.plot(micro_dates, np.zeros_like(micro_dates), 'ko',
            markerfacecolor='white', markersize=10)
    ax.plot(meso_dates, np.zeros_like(meso_dates), 'ko',
            markerfacecolor='tab:red', markersize=10)

    # Annotate the lines.
    for date, level, release in zip(dates, levels, releases):
        version_str = '.'.join(release)
        ax.annotate(version_str, xy=(date, level),
                    xytext=(-3, np.sign(level)*3), textcoords="offset points",
                    verticalalignment="bottom" if level > 0 else "top",
                    fontsize=24,
                    weight='bold' if is_feature(release) else 'normal',
                    bbox=dict(boxstyle='round', pad=0.1, lw=0, fc=(1, 1, 1, 0.7)))

    # Format xaxis with yearly intervals.
    ax.xaxis.set(major_locator=mdates.YearLocator(),
                 major_formatter=mdates.DateFormatter("%Y"))
    plt.setp(ax.get_xticklabels(), fontsize=24)

    # Remove the y-axis and some spines.
    ax.yaxis.set_visible(False)
    ax.spines[["left", "top", "right"]].set_visible(False)

    ax.margins(y=0.1)

    this_scipy = datetime(2024, 7, 10)
    last_scipy = datetime(2023, 7, 12)

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
        t = fig.text(0.05, 0.6 - 0.3*i, link, fontsize=40)
        t.set_url(link)
        add_qrcode(fig, link, [0.7, 0.35 - 0.35*i, 0.3, 0.3])

    return fig


def slides(mpl_path):
    return (
        logo(),
        timeline(mpl_path),
        section_text(),
    )
