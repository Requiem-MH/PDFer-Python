import os
import re
from splitter import Splitter

expressions = {
    'ssid': r'SSID:\s*(\d\d\d\d\d\d\d)',
    'name': r'Student Name:\s*(([\ A-Za-z][A-Za-z\'\-]+\,?)*)'
}

source = '/Users/michaelharrop/Downloads/2015/Batch 1.pdf'
destination = '/Users/michaelharrop/Projects/Work/Split/'
gen_name = '_Transcript.pdf'

split_pdf = Splitter(source, destination, 'Test')
# split_pdf.split(npages=4)
split_pdf.split_on_text(expressions['name'])
#
# count = 0
# for root, dirs, files in os.walk(source):
# for name in files:
#     basename, extension = os.path.splitext(name)
#
#     # Check and open PDFs
#     if extension == '.pdf':
#         count += 1
#         print(name + '\n')
#
#         # Open PDF
#         full_file_path = os.path.join(root, name)
#         opened_pdf = PyPDF2.PdfFileReader(full_file_path, strict=False)
#         print("Working on {i}".format(i=full_file_path))
#
# # Break so it doesn't go into sub-directories
# break
#
# if count == 0:
# print("No PDFs found, please check directory and try again")
#
# else:
# print("Total files worked on: {}".format(count))