# Solution for leg
Even though there is no return value in each of the functions `key1()`, `key2()` and `key3()`, they do return some value, and it is related to the assembly code that is being called in each of them.

We were given the C code and its disassembly externally.
In assembly x86, the register that contains the return value of a function is `rax`, and in ARM architecture (which is the one we're working with in this challenge) is `r0`.

In order to get the flag, we need to enter the program a number that is equal to the sum of the return values of the three functions.
The way to know what each of these functions return, is to view the disassembly.
For each of the functions, we need to see what is the value that is being moved into the `r0` register.

## key1()
```
0x00008cdc <+8>:	mov	r3, pc
0x00008ce0 <+12>:	mov	r0, r3
0x00008ce4 <+16>:	sub	sp, r11, #0
```
Because of pipeline, the value of `pc` will be `0x8ce4`.
## key2()
```
0x00008d04 <+20>:	mov	r3, pc
0x00008d06 <+22>:	adds	r3, #4
0x00008d08 <+24>:	push	{r3}
```
Pipeline again, `pc` is `0x8d0c`.
## key3()
```
0x00008d28 <+8>:	mov	r3, lr
0x00008d2c <+12>:	mov	r0, r3
```
Now the value of the `lr` register will be loaded into the `r3` register. `lr` is the register that contains the return address of the function, which means the address of the instruction that comes after the instruction that called the function.
Let's take a look at the `main` function:
```
0x00008d7c <+64>:	bl	0x8d20 <key3>
0x00008d80 <+68>:	mov	r3, r0
```
We can see that the value of the `lr` register in `key3()` is `0x8d80`.

## Finding The Value
The total value is: `0x8ce4` + `0x8d0c` + `0x8d80` = `108400`.
Now we know what is the value we need to enter in the input in order to get the flag.
