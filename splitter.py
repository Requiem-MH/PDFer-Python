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
        save_name = None

        for i in range(0, self.pdf.getNumPages()):
            # Extract the text from each page
            page = self.pdf.getPage(i)
            page_text = page.extractText()

            # Check for blank pages
            if page_text.strip() == "":
                print(f"Page {i + 1} is a blank. Excluding blank page")
                continue

            print(f"Working on Page {i + 1}")

            # Search page with regex_text
            search_result = re.search(f'{regex_text}', page_text)
            print(search_result)

            if save_name is not None:
                if search_result is None or search_result != save_name:
                    # Save existing output
                    save_pdf.write(f'{self.save_pdf_path}/{save_name}_{self.generic_name}.pdf')
                    save_pdf = PyPDF2.PdfWriter()

            save_pdf.addPage(self.pdf.getPage(i))
            save_name = search_result.group(1) if search_result is not None and search_result.group(1).strip() != "" else f'pg{i + 1}'

        # Save existing output for last page
        save_pdf.write(f'{self.save_pdf_path}/{save_name}_{self.generic_name}.pdf')

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
