class OldPrinter:
    def print_old(self, msg): print("Old printer:", msg)

class PrinterAdapter:
    def __init__(self, old_printer): self.old = old_printer
    def print(self, msg): self.old.print_old(msg)

printer = PrinterAdapter(OldPrinter())
printer.print("Xin chào")
