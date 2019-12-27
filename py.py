import sys 

print('here is python practice: \n')

class text:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
# print(text.BOLD + 'Hello World !' + text.END)

class cards:
    Club = '\u2663'
    Spade = '\u2660'
    Diamond = '\u2666'
    Heart = '\u2665'

# print(cards.Club)

if len(sys.argv)>1:
    if sys.argv[1] == 'types':    
        print('-'*33) 
        print('\n')   
        print('Python types: \n')
        print('Numeric: integer, float, complex')
        print('Sequence: list, tuple, range')
        print('Binary: byte, bytearry')
        print('True/False: bool')
        print('Text: String')
        print('\n')
        print('-'*33)    
    elif sys.argv[1] == 'arithmetic':
        print('-'*33) 
        print('\n')
        print('Arithmetic operators in Python:(by precedence) \n')
        print('1. Exponentiation --- **')
        print('2. Multiplication (division) --- * (/)')
        print('3. Addition (subtraction) --- + (-)')
        print('\n')
        print('-'*33)
    elif sys.argv[1] == 'tips':
        print('-'*33) 
        print('\n')
        print('1. Everything in Python is an object.') 
        print('2. print() with placeholder by using "f": \n')
        print('print(f"Data is {placeholder})"')   
        print('''
            Excepted result is My name is Sherry.
            name = "sherry"
            print(f"My name is {str.capitalize(name)})
        ''') 
        name = 'sherry'   
        print(f"My name is {str.capitalize(name)}")
        print('\n---------------------------------')    
        
    elif sys.argv[1] == 'format':
        print('-'*33) 
        print('\n')
        print('1.text \n2.color')
        print('\n(For instance: text.BOLD + "Hello World !" + text.END)')
        print('\n')
        print('-'*33)
        cur_option = input('please type the number of above items: ')
        if cur_option == '1':
            print('\n------------ text - format -----------\n')
            print('BOLD = \"\\033[1m"\t'+text.BOLD,'Bold',text.END+'\nUNDERLINE = \"\\033[4m"\t'+text.UNDERLINE,'Underline',text.END)
            print('\n------------ end -----------\n')
            # is_continue = input('continue? (Y/N): ')
            # if is_continue == 'y':
            #     cur_option = '2'
                
        elif cur_option == '2':
            print('\n------------ color - format -----------\n')
            print('PURPLE = "\\033[95m"\t'+text.PURPLE,cards.Heart,text.END+'\nCYAN = "\\033[96m"\t'+text.CYAN,cards.Heart,text.END+'\nDARKCYAN = "\\033[36m"\t'+text.DARKCYAN,cards.Heart,text.END+'\nBLUE = "\\033[94m"\t'+text.BLUE,cards.Heart,text.END+'\nGREEN = "\\033[92m"\t'+text.GREEN,cards.Heart,text.END+'\nYELLOW = "\\033[93m"\t'+text.YELLOW,cards.Heart,text.END+'\nRED = "\\033[91m"\t'+text.RED,cards.Heart,text.END+'')
            print('\n------------ end -----------\n')      
    elif sys.argv[1] == 'eg':
        if len(sys.argv) > 2 and sys.argv[2] == '1.1':            
            print('-'*33) 
            print('\n')
            print('"is" and "=="\n')
            print('3 is 3.0 :', 3 is 3.0, '("is" if the references point to the same object)') 
            print('3 == 3.0 :', 3 == 3.0, '("==" tests for equality)')
            print('\n')
            print('-'*33)
    elif sys.argv[1] == 'def':
        if len(sys.argv) > 2 :
            _list = list(sys.argv[2].split(','))
            print(_list)


# print('-'*33) 
        print('\n')
# print('\n---------------------------------') 