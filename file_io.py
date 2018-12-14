# File Modes:
# r  - (default)    read,               pointer at beginning
# w  -              write,              pointer at beginning,   creates a new file if not exist,    overrides existing content
# a  -              append,             pointer at end,         creates a new file if not exist
# b  -              binary
# r+ -              read and write,     pointer at beginning
# w+ -              write and read,     pointer at beginning,   creates a new file if not exist,    overrides existing content
# a+ -              append and read,    pointer at end,         creates a new file if not exist
#
# Buffering
# 0, < 0 - (default)    No buffering
# 1      -              Buffering enabled while accessing file
# > 1    -              Considered as buffer size


file = open('SampleTextFile.txt', 'r')
print('Name:', file.name)
print('Closed?:', file.closed)
print('Access mode:', file.mode)
print('Content:', file.read())
file.close()

# file = open('output.txt', 'w')
# file.write('Hello World to file\nAdding a new line')
# file.close()
#
# file = open('output.txt', 'a')
# file.write('\nAdding another new line')
# file.close()