from pypdf import PdfReader, PdfWriter
import re

class Splitter:
    def __init__(self, pdf_path, save_path, pdf_generic_name):
        self.pdf_path = pdf_path
        self.save_pdf_path = save_path
        self.generic_name = pdf_generic_name.replace('.pdf', '')

        # Initialize PDF Reader
        self.pdf = PdfReader(pdf_path)

    def split(self, npages=1):
        save_pdf = None
        save_pdf_name = None

        for i in range(0, len(self.pdf.pages)):
            # Extract the text from each page
            page = self.pdf.pages[i]
            page_text = page.extract_text()

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

                save_pdf = PdfWriter()
                save_pdf_name = f'1-pg{i + 1}_{self.generic_name}'

            save_pdf.add_page(self.pdf.pages[i])

        # Save existing output before ending
        save_pdf.write(f'{self.save_pdf_path}/{save_pdf_name}.pdf')
