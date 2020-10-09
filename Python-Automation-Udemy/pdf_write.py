# You cannot change individual text in a particular page with PyPDF2.
# However, you can combine and reoder stuff.

# Here we will combine two different PDFs.
import PyPDF2

pdf1File = open('pdf_files/meetingminutes1.pdf', 'rb')
pdf2File = open('pdf_files/meetingminutes2.pdf', 'rb')

# Read pdfs object
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# Write pdf object
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('pdf_files/combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
