#!/usr/bin/env python3

#
# From https://github.com/marcan2020/shc-decoder-poc
#    More decode Information at;
#        https://marcan2020.medium.com/reversing-smart-health-cards-e765157fae9
#
#
# Updated to print JSON info in "pretty" format - Craig Miller 8 Sept 2021
# And read QR Code from PNG file (from greenpass.py https://gir.st/blog/greenpass.html) 
#	./shc-decoder-png.py <png file>
#


import base64
import re
import zlib
import json
import sys
import glob
import os
from PIL import Image
from pyzbar import pyzbar
import base45

VERSION = '1.0.1'

qr_data = ""


# From greenpass.py - decodes QR Code from PNG file

if len(sys.argv) < 2:
    try:
        infile = glob.glob("COVID-19-*-*-*.pdf")[0]
        print(f"Warning: using file {found}, since not specified\n", file=sys.stderr)
    except:
        print(f"Usage: {sys.argv[0]} COVID-19-*-*-*.pdf", file=sys.stderr)
        print(f"Usage: {sys.argv[0]} QR_CODE.png", file=sys.stderr)
        print(f"Usage: {sys.argv[0]} 'shc:/.....'", file=sys.stderr)
        print(f"Version: ", VERSION, file=sys.stderr)
        sys.exit(1)
else:
    if os.path.exists(sys.argv[1]):
        infile = sys.argv[1]
    else:
        infile = None
        qr_data_zlib_b45 = sys.argv[1]

if infile:
    if open(infile, "rb").read(4) == b"%PDF":
        # extract QR code from PDF using hard-coded index, size and bit depth.
        # This will only work with the official Austrian green pass PDFs.
        pdf=PyPDF2.PdfFileReader(open(infile, "rb"))
        qr_img = pdf.getPage(0)['/Resources']['/XObject']['/Im3']
        qr_pil = Image.frombytes("1", (400,400), qr_img.getData())
    else: # assume image
        qr_pil = Image.open(infile)

    # decode QR code into raw bytes:
    qr_data_zlib_b45 = pyzbar.decode(qr_pil)[0].data

print("QR Data:")
print(qr_data_zlib_b45)

# Pass QR Code data to shc-decoder-poc.py code
qr_data = qr_data_zlib_b45


# Create list of data, stripping off 'shc:/'
parts = re.findall(b'..', qr_data[5:])

# Add 45 to each char in data (to prep for base64url function)
jws = ""
for p in parts:
    jws += chr(int(p)+ 45)
    
# JSON Web Signature - See RFC 7515 https://datatracker.ietf.org/doc/html/rfc7515
print("JWS:\n", jws)

def decode(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += "="* (4 - missing_padding)
    return base64.urlsafe_b64decode(data)

jws_parts = list(map(decode, jws.split(".")))

print("JWS Header:")
print(jws_parts[0])

# Use RAW zlib decompression of jws data e.g.wbits=-15 
# https://bugs.python.org/issue5784
shc_data = zlib.decompress(jws_parts[1], wbits=-15)

print("SHC Data:")
#print(shc_data) in "pretty" json format

parsed = json.loads(shc_data)
print(json.dumps(parsed, indent=4, sort_keys=True))




