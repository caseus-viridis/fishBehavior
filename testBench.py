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
import matplotlib.pyplot as P

# parameters
fileName        = "data/Raw data-7 dpf AB in agarose or trap 011015-Trial     5.xlsx"
xVar            = "Trial time (s)"
yVar            = "Activity continuous ()"

# load data
record          = noldusDataIO.dataImport(fileName)
# measurement channels
chan            = record.keys()
nChan           = len(chan)
# plot all measurement channels
ax = []
for i in xrange(nChan):
    ax.append(P.subplot(nChan, 1, i+1))
    x, y = record[chan[i]]['data'][xVar], record[chan[i]]['data'][yVar]
    P.plot(x, y)
    P.title(chan[i])
    P.xlabel(xVar)
    P.ylabel(yVar)
P.show()
