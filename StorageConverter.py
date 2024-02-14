print("Digital Storage Converter")
print("Select what Storage Format to Convert from")
# Selecting Conversion
fconversion = int(input("(1)=Bytes, (2)=Kilobytes, (3)=Megabytes, (4)=Gigabytes, (5)=Terabytes, (6)=Petabytes: "))
print("Select what Storage Format to Convert to")
sconversion = int(input("(1)=Bytes, (2)=Kilobytes, (3)=Megabytes, (4)=Gigabytes, (5)=Terabytes, (6)=Petabytes: "))
# If statements to make stuff work
first = float(input())
# Bytes
if fconversion == 1:
    if sconversion == 1:
        print("Cannot Convert to Same Format")
    if sconversion == 2:
        danswer = first / 1000
        print(danswer,"Kilobytes")
    if sconversion == 3:
        danswer = first / 1000000
        print(danswer,"Megabytes")
    if sconversion == 4:
        danswer = first / 1000000000
        print(danswer,"Gigabytes")
    if sconversion == 5:
        danswer = first / 1000000000000
        print(danswer,"Terabytes")
    if sconversion == 6:
        danswer = first / 1000000000000000
        print(danswer,"Petabytes")
# Kilobytes
if fconversion == 2:
    if sconversion == 1:
        danswer = first * 1000
        print(danswer,"Bytes")
    if sconversion == 2:
        print("Cannot Convert to Same Format")
    if sconversion == 3:
        danswer = first / 1000
        print(danswer,"Megabytes")
    if sconversion == 4:
        danswer = first / 1000000
        print(danswer,"Gigabytes")
    if sconversion == 5:
        danswer = first / 1000000000
        print(danswer,"Terabytes")
    if sconversion == 6:
        danswer = first / 1000000000000
        print(dawnser,"Petabytes")
# Megabytes
if fconversion == 3:
    if sconversion == 1:
        danswer = first * 1000000
        print(danswer,"Bytes")
    if sconversion == 2:
        danswer = first * 1000
        print(danswer,"Kilobytes")
    if sconversion == 3:
        print("Cannot Convert to Same Format")
    if sconversion == 4:
        danswer = first / 1000
        print(danswer,"Gigabytes")
    if sconversion == 5:
        danswer = first / 1000000
        print(danswer,"Terabytes")
    if sconversion == 6:
        danswer = first / 1000000000
        print(danswer,"Petabytes")
# Gigabytes
if fconversion == 4:
    if sconversion == 1:
        danswer = first * 1000000000
        print(danswer,"Bytes")
    if sconversion == 2:
        danswer - first * 1000000
        print(danswer,"Kilobytes")
    if sconversion == 3:
        danswer = first * 1000
        print(danswer,"Megabytes")
    if sconversion == 4:
        print("Cannot Convert to Same Format")
    if sconversion == 5:
        danswer = first / 1000
        print(danswer,"Terabytes")
    if sconversion == 6:
        danswer = first / 1000000
        print(danswer,"Petabytes")
# Terabytes
if fconversion == 5:
    if sconversion == 1:
        danswer = first * 1000000000000
        print(danswer,"Bytes")
    if sconversion == 2:
        danswer = first * 1000000000
        print(danswer,"Kilobytes")
    if sconversion == 3:
        danswer = first * 1000000
        print(danswer,"Megabytes")
    if sconversion == 4:
        danswer = first * 1000
        print(danswer,"Gigabytes")
    if sconversion == 5:
        print("Cannot Convert to Same Format")
    if sconversion == 6:
        danswer = first / 1000
        print(danswer,"Petabytes")
# Petabytes
if fconversion == 6:
    if sconversion == 1:
        danswer = first * 1000000000000000
        print(danswer,"Bytes")
    if sconversion == 2:
        danswer = first * 1000000000000
        print(danswer,"Kilobytes")
    if sconversion == 3:
        danswer = first * 1000000000
        print(danswer,"Megabytes")
    if sconversion == 4:
        danswer = first * 1000000
        print(danswer,"Gigabytes")
    if sconversion == 5:
        danswer = first * 1000
        print(danswer,"Terabytes")
    if sconversion == 6:
        print("Cannot Convert the Same Format")
