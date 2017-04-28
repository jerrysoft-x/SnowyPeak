import os
p = r'C:/Users/JJLI/Documents/GitHub/SnowyPeak/IO/file2.py'
print(os.path.split(p))
print(os.path.splitext(p)[-1])
print(os.path.splitdrive(p))