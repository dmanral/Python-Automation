import PyPDF2

# rb = read binary mode (PDFs are binary files); default = read mode
pdfFile = open('pdf_files/meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

# Returns number of total pages.
print(reader.numPages)

# Stores content of page 0.
page = reader.getPage(0)

# Returns content of page 0.
# print(page.extractText())

# To get all of the text in pdf.
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
