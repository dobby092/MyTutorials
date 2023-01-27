# Simple program for testing git
def higher():
    """
    Input two numbers and returns the higher one.
    """
    a, b = 'a', 'b'
    while type(a) != int:
        try: a = int(input('First number: '))
        except Exception as e: print('Please, try again.')
    while type(b) != int:
        try: b = int(input('Second number: '))
        except Exception as e: print('Please, try again.')
    if a >= b:
        c = a
    elif a < b:
        c = b
    else:
        print("Something went wrong. It's probably your fault, but let me help you")
        exit
    return print(c)

higher()

