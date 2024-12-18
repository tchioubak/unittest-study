import sys

class StupidDialog :
    def dialog(self) :
        keep_going = True
        while keep_going :
            msg = input("?")
            if msg == "soft" :
                keep_going = False
            elif msg == "hard" :
                sys.exit(1)
            elif msg == "smart" :
                return
            print("got msg", msg)
        print("happy of this little chat")

if __name__ == '__main__' :
    StupidDialog().dialog()
