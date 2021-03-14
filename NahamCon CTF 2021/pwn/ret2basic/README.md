# ret2basic

A classic buffer overflow. The binary uses a **_gets_** function to read user input.

There is a function called **give_flag**. This makes our task easier becuase this function will output the flag.
Since PIE is not enabled all we need to do put in  the instruction pointer the memory address of this function.

We have a biffer of 112 chars but to reach EIP we need 120 (112 +8) because is a 64-bit binary and we need to overwrite EBP too.

112 - Buffer's size
8 - size of EBP in memory is 8 bytes

Payload = buffer's size + EBP size + give_flag address

[solve.py](https://github.com/s4nkx0k/CTFs/blob/main/NahamCon%20CTF%202021/pwn/ret2basic/solve.py)
