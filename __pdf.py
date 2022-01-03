import PyPDF2


pdf_file = open('file_name', 'rb')  # it open the file in read-binary format
read_pdf = PyPDF2.PdfFileReader(pdf_file)  # it read the file
print(read_pdf.getDocumentInfo())  # it take the info ot the pdf
number_pages = read_pdf.getNumPages()  # it take the number of pages in the pdf
page = read_pdf.getPage(0)  # it take the content of page 0
page_content = page.extractText()  # it take the text format
print(page_content)  # print the data
