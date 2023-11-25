# Solution of asm
From the code in `asm.c` we can understand that a new page file is created at address `0x41414000` with the size of `0x1000`, and that the binary will execute our x86_64 shellcode.
In the `readme` file we understand that we should only use the syscalls `open()`, `read()` and `write()`.

So the in the file `print_flag.asm` I wrote a shellcode that open the flag file, reads its contents, and writes them into stdout.
