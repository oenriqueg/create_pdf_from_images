import glob
from fpdf import FPDF 

author = 'Oscar Enrique Estrada García'
orientation = 'L' #Landscape or 'P' Portrait
format = (279.4,431.8) # Tabloid
units = 'mm'
file_name = input('¿Con qué nombre desea guardar el archivo?')
width = 410
height = 250 # or auto without parameter
x = 12
y = 50
imagelist = glob.glob('capturas/*.png')
header = input('Escribe el encabezado: ')

pdf = FPDF(orientation, units, format)
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.set_author(author)
    pdf.set_font('Arial','',11)
    width_header = pdf.get_string_width(header) + 6 
    pdf.cell(width_header, 9, f'{header}\n', 0, 1, 'C')
    pdf.cell(450,30,f'{image}',0,0,'C')
    pdf.image(image, x,y,width)
    
pdf.output(f'{file_name}.pdf', "F")