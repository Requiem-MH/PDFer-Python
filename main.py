# import os
# import PyPDF2
# import re
#
# def split_pdf():
#     # Use a breakpoint in the code line below to debug your script.
#     source = '/Users/michaelharrop/Projects/Work/'
#     destination = '/Users/michaelharrop/Projects/Work/Split/'
#     pdf_generic_name = '_Transcript'
#
#     count = 0
#     for root, dirs, files in os.walk(source):
#         for name in files:
#             basename, extension = os.path.splitext(name)
#
#             # Check and open PDFs
#             if extension == '.pdf':
#                 count += 1
#                 print(name + '\n')
#
#                 # Open PDF
#                 full_file_path = os.path.join(root, name)
#                 opened_pdf = PyPDF2.PdfFileReader(full_file_path, strict=False)
#                 print("Working on {i}".format(i=full_file_path))
#
#                 save_pdf = None
#                 save_pdf_name = None
#                 save_pdf_grade = None
#
#                 # Access each individual page of PDF
#                 for i in range(0, 5):
#                 # for i in range(0, opened_pdf.getNumPages()):
#
#                     # Extract the text from each page
#                     page_obj = opened_pdf.getPage(i)
#                     page_text = page_obj.extractText()
#
#                     print(page_text)
#
#                     # # Blank Page Check
#                     # if re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text):
#                     #     print("Working on page {i}: {j}".format(i=i, j=re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1)))
#                     #
#                     #     if save_pdf is None:
#                     #         #First page
#                     #         save_pdf = PyPDF2.PdfWriter()
#                     #         save_pdf.addPage(opened_pdf.getPage(i))
#                     #         try:
#                     #             save_pdf_name = re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1)
#                     #             save_pdf_grade = re.search(r'GRADE: (\d*)', page_text).group(1)
#                     #         except TypeError:
#                     #             save_pdf_name = 'Page {}'.format(i)
#                     #             save_pdf_grade = i
#                     #     else:
#                     #         if save_pdf_name == re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1):
#                     #             save_pdf.addPage(opened_pdf.getPage(i))
#                     #
#                     #         else:
#                     #             output = open(destination + save_pdf_name + pdf_generic_name + save_pdf_grade, 'wb')
#                     #             save_pdf.write(output)
#                     #             output.close()
#                     #
#                     #             save_pdf = PyPDF2.PdfWriter()
#                     #             save_pdf.addPage(opened_pdf.getPage(i))
#                     #             try:
#                     #                 save_pdf_name = re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1)
#                     #                 save_pdf_grade = re.search(r'GRADE: (\d*)', page_text).group(1)
#                     #             except TypeError:
#                     #                 save_pdf_name = 'Page {}'.format(i)
#                     #                 save_pdf_grade = i
#                     # else:
#                     #     print("Excluding blank page")
#
#                     # if save_pdf is not None:
#                     #     output = open(destination + save_pdf_name + pdf_generic_name + save_pdf_grade, 'wb')
#                     #     save_pdf.write(output)
#                     #     output.close()
#
#         # Break so it doesn't go into sub-directories
#         break
#
#     if count == 0:
#         print("No PDFs found, please check directory and try again")
#
#     else:
#         print("Total files worked on: {}".format(count))
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     split_pdf()
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pytesseract
from pdf2image import convert_from_path

source = "/Users/michaelharrop/Projects/Work/test.pdf"
destination = "/Users/michaelharrop/Projects/Work"

image_file_list = []

pdf_pages = convert_from_path(source, 900)

print("Conversion Complete. Reading images...")


with open ("/Users/michaelharrop/Projects/Work/transcript.txt", 'w') as text_file:
    i = 1

    for image_file in pdf_pages:
        text = pytesseract.image_to_string(image_file)

        text_file.write(f"MH - Page {i}: \n{text}\n")
        print(f"MH - Page {i}: \n{text}\n")

        # ssid = re.search(r"SSID:\s*(\d\d\d\d\d\d\d)", text)

        # print(f"Page {i}: SSID = {ssid}")
        i += 1