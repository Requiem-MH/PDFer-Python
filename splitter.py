import PyPDF2
import re

class Splitter:
    def __init__(self, pdf_path, save_path, pdf_generic_name):
        self.pdf_path = pdf_path
        self.save_pdf_path = save_path
        self.generic_name = pdf_generic_name.replace('.pdf', '')

        # Initialize PDF Reader
        self.pdf = PyPDF2.PdfFileReader(pdf_path, strict=False)

    def split(self, npages=1):
        save_pdf = None
        save_pdf_name = None

        for i in range(0, self.pdf.getNumPages()):
            # Extract the text from each page
            page = self.pdf.getPage(i)
            page_text = page.extractText()

            # Check for blank pages
            if page_text.strip() == "":
                print(f"Page {i + 1} is a blank. Excluding blank page")
                continue

            print(f"Working on Page {i + 1}")

            #Start new pdf on every npages
            if i % npages == 0:
                if save_pdf is not None:
                    # Save existing output
                    save_pdf.write(f'{self.save_pdf_path}/{save_pdf_name}.pdf')

                save_pdf = PyPDF2.PdfWriter()
                save_pdf_name = f'pg{i + 1}_{self.generic_name}'

            save_pdf.addPage(self.pdf.getPage(i))

        # Save existing output before ending
        save_pdf.write(f'{self.save_pdf_path}/{save_pdf_name}.pdf')

    def split_on_text(self, regex_text):
        save_pdf = PyPDF2.PdfWriter()
        save_pdf_name = None

        for i in range(0, self.pdf.getNumPages()):
            # Extract the text from each page
            page = self.pdf.getPage(i)
            page_text = page.extractText()

            # Check for blank pages
            if page_text.strip() == "":
                print(f"Page {i + 1} is a blank. Excluding blank page")
                continue

            print(f"Working on Page {i + 1}")

            # Search page for split text
            split_text = re.search(f'{regex_text}', page_text)


            save_pdf_name = f'{split_text.group(1)}_{self.generic_name}' if split_text is not None else f'pg{i + 1}_{self.generic_name}'

            #Search for text in page
            #If text is found, start new document
            #Otherwise add new page
            #Save page

    # if save_pdf is None:
    #     #First page
    #     save_pdf = PyPDF2.PdfWriter()
    #     save_pdf.addPage(opened_pdf.getPage(i))
    #     try:
    #         save_pdf_name = re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1)
    #         save_pdf_grade = re.search(r'GRADE: (\d*)', page_text).group(1)
    #     except TypeError:
    #         save_pdf_name = 'Page {}'.format(i)
    #         save_pdf_grade = i
    # else:
    #     if save_pdf_name == re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1):
    #         save_pdf.addPage(opened_pdf.getPage(i))
    #
    #     else:
    #         output = open(destination + save_pdf_name + pdf_generic_name + save_pdf_grade, 'wb')
    #         save_pdf.write(output)
    #         output.close()
    #
    #         save_pdf = PyPDF2.PdfWriter()
    #         save_pdf.addPage(opened_pdf.getPage(i))
    #         try:
    #             save_pdf_name = re.search(r'STATE ID: (\d\d\d\d\d\d\d)', page_text).group(1)
    #             save_pdf_grade = re.search(r'GRADE: (\d*)', page_text).group(1)
    #         except TypeError:
    #             save_pdf_name = 'Page {}'.format(i)
    #             save_pdf_grade = i
    #
    # if save_pdf is not None:
    #     output = open(destination + save_pdf_name + pdf_generic_name + save_pdf_grade, 'wb')
    #     save_pdf.write(output)
    #     output.close()

    def split_ocr(self):
        pass
        # import re
        # import pytesseract
        # from pdf2image import convert_from_path
        # from PIL import ImageFilter
        #
        # source = "/Users/michaelharrop/Projects/Work/TestDocs/Transcript2.pdf"
        # # destination = "/Users/michaelharrop/Projects/Work/test2.txt"
        #
        # image_file_list = []
        #
        # pdf_pages = convert_from_path(source, 900)
        #
        # print("Conversion Complete. Reading images...")
        #
        # i = 1
        # for image_file in pdf_pages:
        #     image_file.filter(ImageFilter.SHARPEN)
        #     text = pytesseract.image_to_string(image_file)
        #
        #     stu_name = re.search(r"Student Name:\s*(([\ A-Za-z][A-Za-z\'\-_]+\,?)*)", text)
        #     stu_name = stu_name.group(1).replace(' Graduation Year', '') if stu_name is not None else None
        #     grad_year = re.search(r"Graduation Year:\s*(\d\d\d\d)", text)
        #     dob = re.search(r"Date of Birth:\s*(\d\d\/\d\d\/\d\d\d\d)", text)
        #
        #     print(f"Page {i}: Student Name = {stu_name.group(1) if stu_name is not None else None}")
        #     print(f"Page {i}: Graduation Year = {grad_year.group(1)}")
        #     print(f"Page {i}: DOB = {dob.group(1)}")
        #     # print(text)
        #     i += 1

    def split_every_x_pages(self, x):
        pass
