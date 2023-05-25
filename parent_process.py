#parent_process.py
import os
import sys
import time

# Clearing the Screen
os.system('clear')

###SPLIT RANGES###

# Setup the range you want to scan
first = int('2000000000000000', 16)
last = int('3fffffffffffffff', 16)
# Set the number of parts
num_parts = 44

print("Launching {0} child processes for range {1} - {2}".format(num_parts, hex(first), hex(last)))

# Calculate the range size for each part
range_size = last - first + 1
part_size = range_size // num_parts

# Spawn child copies for each part
for part in range(num_parts):
    # Calculate the range for the current part
    part_first = first + (part * part_size)
    part_last = part_first + part_size - 1

    # Adjust the last part to include any remaining values
    if part == num_parts - 1:
        part_last = last

    # Make sure the range is within the boundaries
    part_first = max(part_first, first)
    part_last = min(part_last, last)
    
    # Do something with the child range
    print("Child range {0}: {1} - {2}".format(part + 1, hex(part_first), hex(part_last)))

####LAUNCH CHILD!!!####
    # Spawn a child process with its own console window
    # Construct the command to run the child process in a new terminal window
    script_path = os.path.abspath("child_process.py")
    command = f"python {script_path} {part_first} {part_last}"

    # Open a new terminal window and run the child process
    os.system(f'osascript -e \'tell application "Terminal" to do script "{command}"\'')
