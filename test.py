import fitz
pdf=fitz.open('CBC-sample-report.pdf')
counter=1
text=""
for i in range(len(pdf)):
    page=pdf[i]
    text+=page.get_text()
    
    
with open("test_txt.txt","w",encoding='utf-8') as f:
    f.write(text)
    
    
    
## Fitz Pachhi Karisu Kadach Kales