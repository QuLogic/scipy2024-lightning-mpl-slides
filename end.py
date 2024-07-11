"""
End slides.
"""

import matplotlib.pyplot as plt

from mplslide import slide_heading, add_qrcode


def slides():
    """
    Create end slides.
    """
    fig1 = plt.figure()
    fig1.text(0.5, 0.5, "🎉 And that's all we need! 🎉",
              horizontalalignment='center')

    fig2 = plt.figure()
    fig2.text(0.5, 0.5, 'Was that a good idea?',
              horizontalalignment='center')

    fig3 = plt.figure()
    slide_heading(fig3, 'Bonus: QR codes')
    fig3.text(0.05, 0.05, '''\
import segno
qrcode = segno.make(url)
out = io.BytesIO()
qrcode.save(out, kind='png', dark=MPL_BLUE)
out.seek(0)
img = Image.open(out).convert('RGB')
ax = fig.add_axes(
    location, frameon=False, xticks=[], yticks=[])
ax.imshow(img)''')
    add_qrcode(fig3, 'https://matplotlib.org', [0.55, 0.55, 0.4, 0.4])

    fig4 = plt.figure()
    fig4.text(0.5, 0.8, 'Demo',
              horizontalalignment='center')
    demo_url = 'https://github.com/QuLogic/scipy2024-lightning-mpl-slides'
    t = fig4.text(0.5, 0.7, demo_url,
                  fontsize=48, horizontalalignment='center')
    t.set_url(demo_url)
    add_qrcode(fig4, demo_url, [0.2, 0.1, 0.6, 0.6])

    return (
        fig1,
        fig2,
        fig3,
        fig4,
    )
