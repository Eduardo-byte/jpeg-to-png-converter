import PyPDF2

# with open('pdf_files/dummy.pdf' , 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     #print(len(reader.pages))
#     page = reader.pages[0]
#     #print(reader.pages[0])
#     page.rotate(180)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('pdf_files/tilt.pdf'  , 'wb') as new_file:
#         writer.write(new_file)      

pdf_list = ['pdf_files/dummy.pdf' , 'pdf_files/twopage.pdf' , 'pdf_files/tilt.pdf']

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('pdf_files/super.pdf')
        
pdf_combiner(pdf_list)