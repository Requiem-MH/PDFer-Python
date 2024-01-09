import os
import re
from splitter import Splitter


def main():
    expressions = {
        'ssid': r'SSID:\s*(\d\d\d\d\d\d\d)',
        'name': r'Student Name:\s*(([\ A-Za-z][A-Za-z\'\-]+\,?)*)'
    }

    source = '/Users/michaelharrop/Downloads/2014/Batch 1.pdf'
    destination = '/Users/michaelharrop/Projects/Work/Split/'
    gen_name = '2014_Sky View High School_Transcript'

    split_pdf = Splitter(source, destination, gen_name)
    split_pdf.split()


if __name__ == '__main__':
    main()
