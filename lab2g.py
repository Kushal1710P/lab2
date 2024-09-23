#!/usr/bin/env python3

# Author: Kushal Parmar
# Author ID: kparmar24
# Date Created: 2024/09/23

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(f'{timer}')
    timer -= 1

print('blast off!')
