from pwn import *
from pwnlib.tubes.remote import remote as rmt

def num(output):
        return int(output.split('=')[1].split(' ')[0])

def success_index(output):
        return int(output[output.index('(')+1:output.index(')')])


def half(low, high):
        return ' '.join([str(num) for num in range(low, high+1)])

def found_counterfeit(num, r):
        while True:
                r.sendline(num.encode())
                output = r.recvuntil('\n', True).decode()
                if 'Correct!' in output:
                        return output

def send_nums_recv_weight(nums, r):
        r.sendline(nums.encode())
        return r.recvuntil('\n', True).decode()

def bin_search(N, r):
        low = 0
        high = N - 1
        mid = 0
        while low <= high:
                mid = (low + high) // 2
                nums = half(low, mid)
                output = send_nums_recv_weight(nums, r)
                if nums.count(' ') == 0:
                        if output == '10':
                                low = mid + 1
                                continue
                        if output == '9':
                                output = found_counterfeit(nums, r)
                        #print(nums)
                        print(output)
                        return success_index(output)
                if output[-1] == '9':
                        high = mid
                elif output[-1] == '0':
                        low = mid + 1
                else:
                        exit()
        return -1


def main():
        context(arch='i386', os='linux')

        r = remote('localhost', 9007)
        print(r.recv().decode())
        success = 0
        while success < 100:
                output = r.recv().decode()
                print(output)
                success = bin_search(num(output), r)



if __name__ == '__main__':
        main()
