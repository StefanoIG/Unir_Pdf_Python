import PyPDF2

archivos=[ #Se debe subir los archivos a juntar en la carpeta y luego ponerlos en este arreglo
            "Pdf1.pdf",
            "Pdf2.pdf"]
#Aqui se guarda los pdf unidos
nombre_salida="pdf_unido.pdf"

#Funcion de ensamblador
pdf_final=PyPDF2.PdfMerger()

for nombre_archivo in archivos:
    #Une los pdfs
    pdf_final.append(nombre_archivo)


pdf_final.write(nombre_salida)
pdf_final.close()
