@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/pdfmerge', methods = ['GET', 'POST'])
def upload_files():
   pdfWriter = PyPDF2.PdfWriter()
   if request.method == 'POST':
      files_to_upload = request.files.getlist("file")
      print(files_to_upload)
      for item in files_to_upload:
         f = item
         f.save(secure_filename(f.filename))
         pdfFileObj = open(f.filename, 'rb')
         reader = PyPDF2.PdfReader(pdfFileObj)
         for page_number in range(len(reader.pages)):
            pageObj = reader.pages[page_number]
            pdfWriter.add_page(pageObj) #use add_page
   date = str(now.strftime("%Y-%m-%d"))
   # rand = str(random.randint(1,10000))
   seq = date
   file_name_pdf = 'Merged-'+seq+'.pdf'
   pdfOutput=open(file_name_pdf,'wb')
   pdfWriter.write(pdfOutput)
   pdfOutput.close()
   return app.send_static_file(file_name_pdf)

# Update code to extract text from PDF
# @app.route('/pdftext', methods = ['GET', 'POST'])

if __name__ == '__main__':
   app.run('192.168.156.205')