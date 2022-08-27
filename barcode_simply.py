# Barcode Simply
 
# Barcode - Generating barcodes

from barcode import EAN13
from barcode.writer import ImageWriter


with open(r'C:\Users\deivi\OneDrive\Área de Trabalho\Projets_2022\Project_07\barcodes.png', 'wb') as f: EAN13('123456789012', writer=ImageWriter()).write(f)