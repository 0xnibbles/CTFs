# ret2basic

A classif buffer overflow. The binary uses a **_gets_** function to read user input.

There is a function called **give_flag**. This makes our task easier becuase this function will output the flag.
Since PIE is not enabled all we need to do put in  the instruction pointer the memory address of this function.

[solve.py](https://github.com/s4nkx0k/CTFs/blob/main/NahamCon%20CTF%202021/pwn/ret2basic/solve.py)
