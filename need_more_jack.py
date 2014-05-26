import scipy
import pylab

EPS = {}
COLOR = {}

#-----------#
# S03       #
#-----------#

# E18
t = scipy.zeros(43 * 60 + 3)
t[2 * 60 + 50:] = True
t[5 * 60 + 45:] = False
t[7 * 60 + 25:] = True
t[8 * 60 + 15:] = False
t[9 * 60 + 0:] = True
t[11 * 60 + 10:] = False
t[11 * 60 + 30:] = True
t[12 * 60 + 35:] = False
t[17 * 60 + 40:] = True
t[18 * 60 + 55:] = False
t[19 * 60 + 15:] = True
t[20 * 60 + 10:] = False
t[23 * 60 + 10:] = True
t[24 * 60 + 55:] = False
t[26 * 60 + 15:] = True
t[27 * 60 + 55:] = False
t[30 * 60 + 15:] = True
t[31 * 60 + 35:] = False
t[34 * 60 + 50:] = True
t[36 * 60 + 0:] = False
t[37 * 60 + 55:] = True
t[42 * 60 + 40:] = False
EPS['s03e18'] = t
COLOR['s03e18'] = 'green'

#-----------#
# S06       #
#-----------#

# E19
t = scipy.zeros(43 * 60 + 43)
t[4 * 60 + 25:] = True
t[5 * 60 + 15:] = False
t[9 * 60 + 35:] = True
t[10 * 60 + 20:] = False
t[20 * 60 + 10:] = True
t[21 * 60 + 25:] = False
t[24 * 60 + 45:] = True
t[26 * 60 + 15:] = False
t[30 * 60 + 15:] = True
t[30 * 60 + 25:] = False
t[35 * 60 + 45:] = True
t[38 * 60 + 35:] = False
t[39 * 60 + 00:] = True
t[39 * 60 + 15:] = False
t[40 * 60 + 45:] = True
t[42 * 60 + 55:] = False
EPS['s06e19'] = t
COLOR['s06e19'] = 'red'

# E20
t = scipy.zeros(43 * 60 + 47)
t[2 * 60 + 30:] = True
t[2 * 60 + 50:] = False
t[5 * 60 + 55:] = True
t[6 * 60 + 40:] = False
t[18 * 60 + 30:] = True
t[19 * 60 + 10:] = False
t[26 * 60 + 0:] = True
t[28 * 60 + 0:] = False
t[29 * 60 + 45:] = True
t[35 * 60 + 15:] = False
t[41 * 60 + 30:] = True
t[43 * 60 + 0:] = False
EPS['s06e20'] = t
COLOR['s06e20'] = 'red'


#-----------#
# S09       #
#-----------#

# E01
t = scipy.zeros(44 * 60 + 32)
t[2 * 60 + 15:] = True
t[6 * 60 + 21:] = False
t[14 * 60 + 6:] = True
t[14 * 60 + 20:] = False
t[17 * 60 + 40:] = True
t[19 * 60 + 30:] = False
t[28 * 60 + 45:] = True
t[36 * 60 + 50:] = False
t[40 * 60 + 20:] = True
t[41 * 60 + 35:] = False
EPS['s09e01'] = t
COLOR['s09e01'] = 'blue'

# E04
t = scipy.zeros(43 * 60 + 49)
t[2 * 60 + 16:] = True
t[3 * 60 + 10:] = False
t[5 * 60 + 18:] = True
t[7 * 60 + 35:] = False
t[8 * 60 + 15:] = True
t[9 * 60 + 6:] = False
t[12 * 60 + 50:] = True
t[15 * 60 + 10:] = False
t[19 * 60 + 25:] = True
t[20 * 60 + 20:] = False
t[29 * 60 + 25:] = True
t[32 * 60 + 10:] = False
t[38 * 60 + 15:] = True
t[39 * 60 + 20:] = False
t[39 * 60 + 55:] = True
t[42 * 60 + 15:] = False
EPS['s09e04'] = t
COLOR['s09e04'] = 'blue'


#-----------#
# Analysis  #
#-----------#

def total_fractional_time(t):
    """ Return the total fractional time on screen """
    return sum(t) / len(t)


def average_duration(t):
    """ Return the average duration of an appearance on screen """
    return scipy.average(get_appearances(t))


def std_duration(t):
    """ std of apparances """
    return scipy.std(get_appearances(t))


def get_appearances(t):
    """ return fractional appearance lengths """
    x = []
    L = len(t)
    start, stop, jackOn = 0, 0, False
    for (i, el) in enumerate(t):
        if el and not jackOn:
            jackOn = True
            start = float(i) / L
        if not el and jackOn:
            jackOn = False
            stop = float(i) / L
            x.append(stop - start)

    return scipy.array(x)


#-----------#
# Plotting  #
#-----------#

def make_plots():
    episode_flow()
    jacktion()
    spacing()


def episode_flow():
    """ side-by-side season plots """
    f = pylab.figure()
    f.subplots_adjust(hspace=0.7)
    N = len(EPS)
    for (i, ep) in enumerate(sorted(EPS.keys())):
        s = f.add_subplot(N, 1, i + 1)
        t = EPS[ep]

        x = scipy.linspace(0, 1, len(t))
        s.plot(x, t,
               lw=2,
               color=COLOR[ep],
               alpha=0.6)

        title = '{} - {:.2%}'.format(ep, total_fractional_time(t))
        s.set_title(title)
        s.set_yticks([0, 1])
        s.set_yticklabels(['no jack', 'jack'])
        s.set_ylim((-0.1, 1.1))
    f.tight_layout()
    f.show()


def jacktion():
    """ Bar chart plot showing fractional time on screen as well as average
        length of appearance and std as error bars

    """
    eps = sorted(EPS.keys())

    epsMean = [average_duration(EPS[ep]) for ep in eps]
    epsStd = [std_duration(EPS[ep]) for ep in eps]
    epsTot = [total_fractional_time(EPS[ep]) for ep in eps]

    barWidth = 0.35
    opacity = 0.4

    errorConfig = {'ecolor': '0.3'}

    f = pylab.figure()
    s = f.add_subplot(111)

    index = scipy.arange(len(eps))
    s.bar(index, epsTot, barWidth,
          alpha=opacity,
          color='b',
          yerr=epsStd / scipy.sqrt(len(eps)),
          error_kw=errorConfig,
          label='Total Jack time')

    s.bar(index + barWidth, epsMean, barWidth,
          alpha=opacity,
          color='r',
          yerr=epsStd,
          error_kw=errorConfig,
          label='Average appearance duration')

    s.set_xlabel('Episodes')
    s.set_ylabel('Percentage of episode')
    s.set_title('Jacktion')
    s.set_xticks(index + barWidth)
    s.set_xticklabels(eps)
    s.legend()

    f.tight_layout()
    f.show()


def spacing():
    """ Histograms of the durations of Jack appearances """
    f = pylab.figure()
    f.subplots_adjust(hspace=0.45)
    N = len(EPS)
    for (i, ep) in enumerate(sorted(EPS.keys())):
        s = f.add_subplot(N, 1, i + 1)
        t = EPS[ep]
        z = sorted(get_appearances(t))
        s.hist(z,
               bins=scipy.linspace(0, .2, 20),
               range=(0, .2),
               color=COLOR[ep],
               alpha=0.4)

        title = '{} - {:.2%}'.format(ep, total_fractional_time(t))
        s.set_title(title)
        s.set_ylim((0, 5.5))
        s.set_xlim((0, .2))
    f.tight_layout()
    f.show()
