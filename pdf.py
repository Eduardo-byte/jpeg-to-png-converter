import PyPDF2
import fitz
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader
from typing import Union, Literal, List

#### rotate file and create a new one with that file###
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

######  combine all the files in the array provided  #######
# pdf_list = ['pdf_files/dummy.pdf' , 'pdf_files/twopage.pdf' , 'pdf_files/tilt.pdf']

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('pdf_files/super.pdf')
        
# pdf_combiner(pdf_list)

#### Delete a page #####
# Path of the PDF file
# input_file = r"pdf_files/Eduardo_Brito_CV_Developer.pdf"
  
# # Path for the output PDF file
# output_file = r"pdf_files/modified_test.pdf"
  
# # Opening the PDF file and creating a handle for it
# file_handle = fitz.open(input_file)
  
# # The page no. denoted by the variable will be deleted
# page = 8
  
# # Passing the variable as an argument
# file_handle.delete_page(page)
  
# # Saving the file
# file_handle.save(output_file)

##### Add a watermark to a pdf ######
def watermark(
    content_pdf: 'pdf_files/super.pdf', 
    stamp_pdf: 'pdf_files/wtr.pdf', 
    pdf_result: 'pdf_files/watered.pdf', 
    page_indices: Union [Literal['ALL'], List[int]] = 'ALL',
):
    try:
        reader = PdfReader(content_pdf)
        if page_indices == "ALL":
            page_indices = list(range(0, len(reader.pages)))

        writer = PdfWriter()
        for index in page_indices:
            content_page = reader.pages[index]
            mediabox = content_page.mediabox

            # You need to load it again, as the last time it was overwritten
            reader_stamp = PdfReader(stamp_pdf)
            image_page = reader_stamp.pages[0]

            image_page.merge_page(content_page)
            image_page.mediabox = mediabox
            writer.add_page(image_page)

        with open(pdf_result, "wb") as fp:
            writer.write(fp)
        print("Watermarking successful. Output saved to:", pdf_result)
    except Exception as e:
        print("Error:", str(e))
        
watermark('pdf_files/super.pdf', 'pdf_files/wtr.pdf', 'pdf_files/watered.pdf')  


### Another way to add the watermark ###
template = PyPDF2.PdfReader(open('pdf_files/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('pdf_files/wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('pdf_files/watermarked_output.pdf', 'wb') as file:
    output.write(file)