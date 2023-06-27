import colorama,cmd
from enum import IntFlag,Flag,auto
from io import BytesIO

from barcode import EAN13
from barcode import ISBN13,UPCA,Code128
from barcode.writer import SVGWriter

class status(IntFlag):
    functional = auto()
    ram = auto()
    gpu = auto()
    wifiAntenna = auto()
    hhd = auto()
    ssd = auto()
class Status(Flag):
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
            with open("gen\\"+name+".svg", "wb") as f:
                Code128(str(10000000000+state+(error*1000)), writer=SVGWriter()).write(f)
            #cairosvg.svg2png(url=name+'.svg', write_to=name+'.png')
            #pygame.image.save(pygame.image.load(name+".svg"),name+".png")
    
    def do_get(self, arg):
        """get then scan barcode"""
        num = int(arg)
        print(num//1000)
        print(((num-((num//1000)*1000))//10))
        print(status((num-((num//1000)*1000))//10))
        st =status((num-((num//1000)*1000))//10)
        print(num-((num//1000)*1000)-1)
        print((num-100000000000)//10000)
        print(int.to_bytes((num-100000000000)//10000,5,"big").decode("ascii"))
        if status.functional in st: print(Status.functional)
        for i in list(status):
            if i in st: 
                print(i)
            else:
                #print("!",i,i & st)
                pass
    def do_scan(self, arg):
        """repeatedly scan barcodes
        Q to quit"""
        i = ""
        while True:
            i = input("Scan>")
            if "q" in i.lower(): break
            try:
                self.do_get(i)
            except:
                print("err reading")

            
#pygame.init()

pc().cmdloop()