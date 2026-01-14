import os
from fpdf import FPDF

def pdf_maker():
    with open("report_card_data.txt","r") as f:
        content = f.read()
        pdf = FPDF("portrait","mm","A4")
        pdf.add_page()
        pdf.set_font("Arial","B",12)
        pdf.multi_cell(0,8,f"{content}",1,"C")
        pdf.output("pdf_report#.pdf")
        print(f"PDF GENERATED SUCCESSFULLY : pdf_report#.pdf !")