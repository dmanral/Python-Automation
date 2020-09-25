"""
Raising exception example:

*************
*           *
*           *
*           *
*************

"""

def boxPrint(symbol, width, height):
    # This is a traceback error.
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('3', 15, 5)
boxPrint('o', 5, 16)
boxPrint('*', 2, 2)

"""
You can write the exception in a log file as well. Here is an example of doing that
via command code:
>>> import traceback
>>> try:
...     raise Exception('This is the error message.')
... except:
...     errorFile = open('to_delete/error_log.txt', 'a')
...     errorFile.write(traceback.format_exc())
...     errorFile.close()
...     print('The traceback info was written in error_log.txt.')
"""
