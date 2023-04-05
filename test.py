from sys import argv

def main(*arg):
    print('----start-----')
    for i in arg:
        print(i, end='\n')
    print('-----end-----')
        
    
if __name__ == '__main__':
    print(len(argv))
    main(argv)
    pass