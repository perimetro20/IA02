# parser for taking the input and turning it into
# common lisp code.
import sys

max_height = int(input())
print(max_height)

for line in sys.stdin:
    stacks = line.split('; ')
    stacks = [stack.strip() for stack in stacks]
    stacks = [stack.replace(',', '') for stack in stacks]
    # stacks = [stack.replace('(', '\'(') for stack in stacks]
    # stacks = [stack.replace('X', '\'X') for stack in stacks]
    print("({0})".format(' '.join(stacks)))