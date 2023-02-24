import os
import re
from splitter import Splitter


def main():
    expressions = {
        'ssid': r'SSID:\s*(\d\d\d\d\d\d\d)',
        'name': r'Student Name:\s*(([\ A-Za-z][A-Za-z\'\-]+\,?)*)'
    }

    source = '/Users/michaelharrop/Downloads/2015/Batch 1.pdf'
    destination = '/Users/michaelharrop/Projects/Work/Split/'
    gen_name = '_Transcript.pdf'

    split_pdf = Splitter(source, destination, 'Test')
    split_pdf.split(npages=4)
    # split_pdf.split_on_text(expressions['name'])


if __name__ == '__main__':
    main()
