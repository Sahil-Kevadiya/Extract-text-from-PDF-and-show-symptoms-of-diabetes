import PyPDF2
from PyPDF2 import PdfReader
import sys
import re
import fitz

reader = PyPDF2.PdfReader("CBC-sample-report.pdf")
# print(reader.metadata)
# print(len(reader.pages))
page = reader.pages[0]
# print("-------------------------------------------------------------------------------", type(str))
a = page.extract_text().lower()
print(a)
he_pattern=re.compile("^ *hemoglobin.*\d+",re.MULTILINE)
wbc_pattern=re.compile("^ *white blood cell.*\d+",re.MULTILINE)
rbc_pattern=re.compile("^ *red blood cell.*\d+",re.MULTILINE)
ptl_pattern=re.compile("^ *platelet count.*\d+",re.MULTILINE)
# print(he_pattern.findall(a))
# print(wbc_pattern.findall(a))
# print(rbc_pattern.findall(a))
# print(ptl_pattern.findall(a))

file = open(sys.argv[1],'x')
file.write(he_pattern.findall(a)[0])
file.write("\n")
file.write(wbc_pattern.findall(a)[0])
file.write("\n")
file.write(rbc_pattern.findall(a)[0])
file.write("\n")
file.write(ptl_pattern.findall(a)[0])
