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

pageStart = 1
pageEnd = maxPages

if len(sys.argv) >= 4:
	pageStart = int(sys.argv[3])

if len(sys.argv) >= 5:
	pageEnd = int(sys.argv[4])

outputBasePath = sys.argv[2]
baseFileName = os.path.splitext(os.path.basename(inputFN))[0]
pageRect = CGRectMake (0, 0, 612, 792)

for pageNumber in range(pageStart,pageEnd+1):
   outputFileName = '%s%s_%02d.pdf' % (outputBasePath, baseFileName, pageNumber)
   writeContext = CGPDFContextCreateWithFilename(outputFileName, pageRect)
   print 'Writing page %d' % pageNumber
   mediaBox = inputDoc.getMediaBox(pageNumber)
   writeContext.beginPage(mediaBox)
   writeContext.drawPDFDocument(mediaBox, inputDoc, pageNumber)
   writeContext.endPage()

print 'Done'