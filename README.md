A pre-alpha version of the label generator

To use, do the below -

 - Install dependent packages

$ pip install svglue pyqrcode cairosvg

 - Add Product details in label.py

    sticker_data = {
        '_first_line': 'Chowka Bara',
        '_second_line': '5 Houses',
        '_price': '900',
        '_url': 'https://rollthedice.in/products/chowka-bara-5-houses-board-game'
    }

 - Most importantly, modify the template for your requirement. Use inkscape and modify the svg.
 - The texts/qr code sections that need to be replaced has to be updated.

    For eg. add a template-id to all the tspans, rects. They've to be unique. This can be updated in a text/code editor. Inkscape's XML editor proved to be clunky.

    <tspan template-id="PPR-40">00000</tspan>

After all is set, run the python code.

$ python label.py

 