from escpos.printer import Usb

def print():
    printer = Usb(0x04b8, 0x0202)  # vendor_id, product_id

    printer.image()
    printer.cut()
    printer.line_spacing()