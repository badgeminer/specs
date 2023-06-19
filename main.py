import colorama,cmd
from enum import IntFlag,auto
from io import BytesIO

from barcode import EAN13
from barcode.writer import SVGWriter

class status(IntFlag):
    functional = auto()
    ram = auto()
    gpu = auto()
    wifiAntenna = auto()
    hhd = auto()
    ssd = auto()

class pc(cmd.Cmd):
    intro = 'PCStatus   Type help or ? to list commands.\n'
    prompt = 'pc>'
    file = None

    # ----- basic turtle commands -----
    def do_make(self, arg):
        """make
        -f functional
        -r has ram
        -g has gpu
        -w has wifi antenna
        -ssd,-hhd has that kind of drive"""
        print(arg)
        print(type(arg))
        state = 0
        error = 0
        name = ""
        args:list[str] = arg.split(" ")
        if "-f" in args: state = state|status.functional
        if "-r" in args: state = state|status.ram
        if "-g" in args: state = state|status.gpu
        if "-w" in args: state = state|status.wifiAntenna
        if "-hhd" in args: state = state|status.hhd
        if "-ssd" in args: state = state|status.ssd
        if "--name" in args:
            name = args[args.index("--name")+1]
        if "--error" in args:
            
            error=int.from_bytes(args[args.index("--error")+1].encode("ascii"),'big')

        if "--name" in args:
            name = args[args.index("--name")+1]
            print(int(status.functional|status.ram|status.gpu|status.wifiAntenna|status.ssd|status.hhd))
            print(int(state))
            print(error*1000)
            # Or to an actual file:
            with open(name+".svg", "wb") as f:
                EAN13(str(100000000000+state+(error*1000)), writer=SVGWriter()).write(f)


pc().cmdloop()