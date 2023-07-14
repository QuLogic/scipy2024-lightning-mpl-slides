"""
End slides.
"""

import matplotlib.pyplot as plt


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
    fig3.text(0.5, 0.5, 'Demo',
              horizontalalignment='center')
    demo_url = 'https://github.com/QuLogic/scipy2023-lightning-mpl-slides'
    t = fig3.text(0.5, 0.4, demo_url,
                  fontsize=48, horizontalalignment='center')
    t.set_url(demo_url)

    return (
        fig1,
        fig2,
        fig3,
    )
