import PyPDF2
import fitz

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

# pdf_list = ['pdf_files/dummy.pdf' , 'pdf_files/twopage.pdf' , 'pdf_files/tilt.pdf']

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('pdf_files/super.pdf')
        
# pdf_combiner(pdf_list)

  
# Path of the PDF file
input_file = r"pdf_files/Eduardo_Brito_CV_Developer.pdf"
  
# Path for the output PDF file
output_file = r"pdf_files/modified_test.pdf"
  
# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)
  
# The page no. denoted by the variable will be deleted
page = 8
  
# Passing the variable as an argument
file_handle.delete_page(page)
  
# Saving the file
file_handle.save(output_file)