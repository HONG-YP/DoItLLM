import pymupdf
import os

pdf_path = "./chap4/data/sony-parsing.pdf"
doc = pymupdf.open(pdf_path)

header_h = 80
footer_h = 80

full_text = ''

for page in doc:
    rect = page.rect
    header = page.get_text(clip = (0, 0, rect.width, header_h))
    footer = page.get_text(clip = (0, rect.height - footer_h, rect.width, rect.height))
    text = page.get_text(clip = (0, header_h, rect.width, rect.height - footer_h))
    full_text += text + '\n-----------------------------------\n'

pdf_file_name = os.path.basename(pdf_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

txt_path = f"./chap4/output/{pdf_file_name}_preprocessed.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(full_text)