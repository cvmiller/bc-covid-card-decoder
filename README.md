# bc-covid-card-decoder
A Python Decoder of the BC Covid Vaccine Card QR Code

Requirements: Python3 & the following libraries
* `pip3 install flynn base45 PyPDF2 pyzbar Pillow`
* Install a `zbar` library for your distro:
	* Redhat/Fedora: `dnf install zbar` 
	* Debian/Ubuntu: `apt install libzbar0` 
	* Alpine Linux:  `apk add libzbar`


Copy QR Code to a File, then run the decoder using the PNG file. It will "pretty" print the JSON data in the QR Code


**Usage:** ./shc-decoder-png.py &lt;QR Code PNG file&gt;

---

Work is based on shc-decoder-poc.py	from [https://github.com/marcan2020/shc-decoder-poc](https://github.com/marcan2020/shc-decoder-poc)
and greenpass.py [https://gir.st/blog/greenpass.html](https://gir.st/blog/greenpass.html)

