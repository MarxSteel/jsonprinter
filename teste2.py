import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('marxtei', 'a8f7360faa2ccb2504320d3b87e0ec4b')

    # configure the conversion
    client.setPageSize('A6')
    client.setNoMargins(True)


    output_file = open('test.pdf', 'wb')

    # run the conversion and store the result into a pdf variable
    pdf = client.convertUrl('http://interactbrasil.org/adam/teste.html')

    # write the pdf the into the output file
    output_file.write(pdf)

    # close the output file
    output_file.close()
except pdfcrowd.Error as why:
    # report the error
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # handle the exception here or rethrow and handle it at a higher level
    raise
