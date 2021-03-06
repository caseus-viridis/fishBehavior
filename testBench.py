#!/usr/bin/python

# --------------------------------------------------------------------------------
# (c) COPYRIGHT 2015 The Salk Institute.  All rights reserved.
#
# The party (the "Recipient") receiving this software directly from the Salk
# Institute may use this software and make copies thereof as reasonably necessary
# solely for the purposes set forth in the agreement between the Recipient and
# the Salk Institute (the "Agreement").  The software may be used in source code
# form solely by the Recipient's employees.  The Recipient shall have no right to
# sublicense, assign, transfer or otherwise provide the source code to any
# third party. Subject to the terms and conditions set forth in the Agreement,
# this software, in binary form only, may be distributed by the Recipient to
# its customers. The Salk Institute retains all ownership rights in and to the
# software.
#
# This notice shall supercede any other notices contained within the software.
#
# Xin Wang <xinw@snl.salk.edu>
# --------------------------------------------------------------------------------

# dependencies
import noldusDataIO
import numpy as N
import matplotlib.pyplot as P

# parameters
fileName        = "data/Raw data-7 dpf AB in agarose or trap 011015-Trial     5.xlsx"
xVar            = "Trial time (s)"
yVar            = "Activity continuous ()"
chan1, chan2    = "Track-left gill-Subject 1", "Track-right gill-Subject 1"

# load data
record          = noldusDataIO.dataImport(fileName)
# measurement channels
chan            = record.keys()
nChan           = len(chan)
# plot all measurement channels
# ax = []
# x, y = [], []
# for i in xrange(nChan):
#     ax.append(P.subplot(nChan, 1, i+1))
#     x.append(record[chan[i]]['data'][xVar])
#     y.append(record[chan[i]]['data'][yVar])
#     P.plot(x[i], y[i])
#     P.title(chan[i])
#     P.xlabel(xVar)
#     P.ylabel(yVar)
# P.show()

x1, y1 = record[chan1]['data'][xVar], record[chan1]['data'][yVar]
x2, y2 = record[chan2]['data'][xVar], record[chan2]['data'][yVar]

y1 = N.interp(x1, x1[~N.isnan(y1)], y1[~N.isnan(y1)])
y2 = N.interp(x2, x2[~N.isnan(y2)], y2[~N.isnan(y2)])

dt = N.mean(N.diff(x1))

xcorr = N.correlate(y1, y2, 'full')
tcorr = dt * N.array(range(-len(xcorr)/2+1, len(xcorr)/2+1))

P.plot(tcorr, xcorr)
P.show()
