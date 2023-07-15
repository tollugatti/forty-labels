#!/usr/bin/env python

import svglue
import pyqrcode, sys
import cairosvg
from pyqrcode import QRCode


# define template file
TEMPLATE="rollthedice-price-sticker-template.svg"

def build_sheet(sticker_data):
    # load the template from a file
    tpl = svglue.load(file=TEMPLATE)
  
    # Generate QR code
    url = pyqrcode.create(sticker_data['_url'])
  
    url.svg("qrcode.svg", scale = 0.5)
    
    for idx in list(range(1, 41)):
        tpl.set_text('PFNA-'+str(idx), sticker_data['_first_line'])
        tpl.set_text('PFNB-'+str(idx), sticker_data['_second_line'])
        tpl.set_text('PPR-'+str(idx), sticker_data['_price'])
        tpl.set_svg('qr-'+str(idx), file='qrcode.svg')



    src = tpl.__str__()
    return src


if __name__ == "__main__":
    
    sticker_data = {
        '_first_line': 'Chowka Bara',
        '_second_line': '5 Houses',
        '_price': '900',
        '_url': 'https://rollthedice.in/products/chowka-bara-5-houses-board-game'
    }

    src = build_sheet(sticker_data)
    
    sheet_name = sticker_data['_first_line'].replace(' ', '_')+'_'+sticker_data['_second_line'].replace(' ', '_')+'.pdf'
    with open(sheet_name, 'wb') as out:
        cairosvg.svg2pdf(bytestring=src, write_to=out)
    

