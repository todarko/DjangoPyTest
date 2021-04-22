

# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('C:\\Users\\tcowdrey.HSA\\Downloads\\death.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 

    
# extracting text from page 

if pdfReader.numPages > 0:
    for Row in range(0,pdfReader.numPages - 1): 
        pageObj = pdfReader.getPage(Row) 
        print(Row)
        print(pageObj.extractText())



    
# closing the pdf file object 
pdfFileObj.close() 