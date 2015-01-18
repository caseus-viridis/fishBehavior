"""
This module contains routines for importing Noldus .xlsx data file.

--------------------------------------------------------------------------------
(c) COPYRIGHT 2015 The Salk Institute.  All rights reserved.

The party (the "Recipient") receiving this software directly from the Salk
Institute may use this software and make copies thereof as reasonably necessary
solely for the purposes set forth in the agreement between the Recipient and
the Salk Institute (the "Agreement").  The software may be used in source code
form solely by the Recipient's employees.  The Recipient shall have no right to
sublicense, assign, transfer or otherwise provide the source code to any
third party. Subject to the terms and conditions set forth in the Agreement,
this software, in binary form only, may be distributed by the Recipient to
its customers. The Salk Institute retains all ownership rights in and to the
software.

This notice shall supercede any other notices contained within the software.

Xin Wang <xinw@snl.salk.edu>
--------------------------------------------------------------------------------
"""

# dependencies
import xlrd         # requires the xlrd package (https://pypi.python.org/pypi/xlrd)
import numpy as N

# import data
def dataImport(fileName, sheetNameList = None):
    """
    Imports data from Noldus .xlsx file.
    """
    print "Opening data file: " + fileName
    # open the workbook from file, let xlrd handle IO exceptions
    wb = xlrd.open_workbook(fileName)
    # get the names of the worksheets
    wsName = sheetNameList or wb.sheet_names()
    # init a dict
    experiment = {}
    # load data
    for wsn in wsName: # iterate through the worksheets
        print "Loading data channel: " + wsn
        experiment[wsn] = {} # specific measurement channel in this sheet
        ws = wb.sheet_by_name(wsn) # worksheet
        # get the header length and data length
        nHeaderLine = int(ws.cell_value(0, 1))
        nRow = ws.nrows
        # read header
        for i in xrange(nHeaderLine-3):
            experiment[wsn][ws.cell_value(i, 0)] = ws.cell_value(i, 1)
        # read main data
        experiment[wsn]['data'] = {} # real data now
        for i in xrange(ws.ncols):
            field = ws.cell_value(nHeaderLine-2, i)+' '+ws.cell_value(nHeaderLine-1, i)
            experiment[wsn]['data'][field] = N.empty([nRow-nHeaderLine, 1])
            for j in xrange(nHeaderLine, nRow):
                if ws.cell_type(j, i) == 2:
                     temp = ws.cell_value(j, i)
                else:
                     temp = N.nan
                experiment[wsn]['data'][field][j-nHeaderLine] = temp
    # output
    print "Completed loading: " + fileName
    return experiment

if __name__ == '__main__':
    pass
