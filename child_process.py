import sys
from bit import Key
import time
import os

# Function to run each part of the range
def process_range(first, last):
    # Clearing the Screen
    os.system('clear')

    print("Processing range:", hex(first), hex(last))
    time.sleep(5)

    # setup the winning address
    WINNING_ADDRESS = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so' #the winning address we want to find
    #TEST_WINNING_ADDRESS = '18ZMbwUFLMHoZBbfpCjUJQTCMCbktshgpe' #test address only

    for num in range(first, last + 1):
        hex_string = hex(num)[2:].upper().zfill(64)        
        #test_hex_string = "000000000000000000000000000000000000000000000001a838b13505b26867" #test key only
        my_key = Key.from_hex(hex_string)
        if my_key.address == WINNING_ADDRESS:
            print('Match found a Winner!!!')
            print('Winning Private Key = ', my_key)
            print('Matched address: ', my_key.address)
            with open("WINNER.txt", 'w') as file:
                file.write("Match found a Winner!!!" + "\n")
                file.write(str(my_key) + "\n")
                file.write(my_key.address)
            os.system('say "Your program has finished"')
            os.system('say "We found a winner"')
            os.system('say "We found a winner"')
            os.system('say "We found a winner"')

# Get the range for this child process from command-line arguments
part_first = int(sys.argv[1])
part_last = int(sys.argv[2])

# Call the process_range function with the current range
process_range(part_first, part_last)
print("PROCESSING COMPLETED FOR RANGE:", hex(part_first), hex(part_last))