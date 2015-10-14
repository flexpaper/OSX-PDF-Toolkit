#!/usr/bin/python

import sys
import os

from CoreGraphics import *


inputFN = sys.argv[1]
inputDoc = \
  CGPDFDocumentCreateWithProvider(\
  CGDataProviderCreateWithFilename(inputFN))

if inputDoc:
  maxPages = inputDoc.getNumberOfPages()
  print '%s has %d pages' % (inputFN, maxPages)
else:
  sys.exit(2)

catRange        = sys.argv[2]
catRangeList	= catRange.split(",")
outputFN 		= sys.argv[3]
baseFileName    = os.path.splitext(os.path.basename(inputFN))[0]

pageRect = CGRectMake (0, 0, 612, 792)
writeContext = CGPDFContextCreateWithFilename(outputFN, pageRect)

for i, val in enumerate(catRangeList):
   pageNumber = int(val);
   print 'Writing page %d' % pageNumber
   #mediaBox = inputDoc.getMediaBox(pageNumber)
   mediaBox = inputDoc.getPage(pageNumber).getBoxRect(kCGPDFBleedBox)
   writeContext.beginPage(mediaBox)
   writeContext.drawPDFDocument(mediaBox, inputDoc, pageNumber)
   writeContext.endPage()
print 'Done'