# bc-covid-card-decoder
A Python Decoder of the BC Covid Vaccine Card QR Code and Canada QR Code

![Canada QR Sample](https://raw.githubusercontent.com/cvmiller/bc-covid-card-decoder/main/fed_can_covid_pvc-specimen-1.jpg)

Requirements: Python3 & the following libraries
* `pip3 install flynn base45 PyPDF2 pyzbar Pillow`
* Install a `zbar` library for your distro:
	* Redhat/Fedora: `dnf install zbar` 
	* Debian/Ubuntu: `apt install libzbar0` 
	* Alpine Linux:  `apk add libzbar`


Copy QR Code to a File, then run the decoder using the PNG file. It will "pretty" print the JSON data in the QR Code


**Usage:** ./shc-decoder-png.py &lt;QR Code PNG file&gt;

---
**Note:** Decoder is designed to reveal the information contained in the QR Code, and does not *validate* the QR Code.

Work is based on shc-decoder-poc.py	from [https://github.com/marcan2020/shc-decoder-poc](https://github.com/marcan2020/shc-decoder-poc)
and greenpass.py [https://gir.st/blog/greenpass.html](https://gir.st/blog/greenpass.html)

