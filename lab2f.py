#!/usr/bin/env python3

#Author: Kushal parmar
#Author_ID: kparmar24
#Date Created: 2024/09/23

import sys 

timer = int(sys.argv[1])

while timer > 0:
    print(f'{timer}')  # Print the current value of the timer with a message
    timer -= 1 
# Print "Blast off!" when the countdown ends
print('blast off!')
