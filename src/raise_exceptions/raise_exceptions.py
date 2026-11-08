'''
raise keyword is used with try catch to raise our own exception when needed. 
raising an exception is a way of saying, "Stop running the code in this function and move the program 
execution to the except statement. 

The code block which uses raise with try except looks like below

def function_name():
    if condition():
        raise Exceptoin("print something")
    if condition("print something"):
        raise Exception()

    try:
        calling_the_function
    except Exception as err:
        print('something')

Example below
'''

'''
Function that takes a symbol, height and width and create a printed box.
'''
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must be single character ascii character")
    if width <= 2 or height <= 2:
        raise Exception("height or width must be greater than 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width  - 2) ) + symbol)
    print(symbol * width)


def test_boxprint(box_data):
    for sym, w, h in (box_data):
        try:
            box_print(sym, w, h)
        except Exception as err:
            print('An exception happened: ' + str(err)) # here err comes from the raise error that our function returns

def main():
    box_data = (('$', 6, 7), ('!', 7, 10), ('"', 20, 5), ('AB', 1, 2), ('&', 10, 2))
    test_boxprint(box_data)

if __name__ == "__main__":
    main()
    


