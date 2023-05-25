# HexadecimalRange_to_BitcoingAddressQuery
A fun project to attempt solving the 1000BTC puzzle https://privatekeys.pw/puzzles/bitcoin-puzzle-tx

To launch install all the dependencies and run:

Python parent_process.py

This process has some hardcoded values you can alter based on the puzzle your trying to solve.

Set the range you want to scan in the code as well as the number of child windows you want to spawn:
first = int('2000000000000000', 16)
last = int('3fffffffffffffff', 16)
num_parts = 44

Range is obviously the range you want to scan. In this case its setup for puzzle 66.
num_parts is the number parts you want to split the range into.

Each part will spawn child_process.py in its own console windows (macos) and will iterate through that range.

Not the most complex application but a fun exercise in chopping up parts of the hexadecimal private key range and realizing the sheer size.

I have not edited the main code to reverse the direction of iteration but have simply including parent_process_reverse.py alter the parameters in that and run it to try solving in reverse.

child_process.py and chile_process_reverse.py have a hardcoded value of the bitcoin address we are trying to match in puzzle 66, if you want to have some fun trying to alter the other puzzles expand your range to that of the reamining prizes and edit the address to match the relevant address for that puzzle.

Potential updates - splitting the address into such a wide range and running iteration in consoles windows is less than optimal but a fun way to mess around with the processes involved.

Future state I may launch a new project taking ideas from here to:
Take a hex range as input
Take number of chunks as input
Take forward scanning, reverse scanning or random scanning as input.
Break range into chunks and spawn a function to convert to bitcoin address and match it against an array of addresses
Ideally we utilize C or C++ and we spawn the child processes off onto graphics cards cores.
Winning finds would write back to the main console and to disk.





