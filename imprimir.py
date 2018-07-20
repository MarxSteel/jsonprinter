

import cups

conn = cups.Connection()
printers = conn.getPrinters()
fileName =  "test.pdf"
conn.printFile("ZJ-58", fileName, " ", {'PageSize':'A6'})
