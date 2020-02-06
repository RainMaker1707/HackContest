import PyPDF4 as Pdf


def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        reader = Pdf.PdfFileReader(input_file)
        reader.decrypt(password)

        writer = Pdf.PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.write(output_file)


def encrypt_pdf(input_pdf, output_pdf, password):
    pdf_writer = Pdf.PdfFileWriter()
    pdf_reader = Pdf.PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(password, '', use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

