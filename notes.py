from sys import argv as args_def
import argparse
import controller
from single_note import single_note
from datetime import *


def main():
    parser = argparse.ArgumentParser(description='This is not a Notepad', add_help=True)
    # parser.add_argument('-not-i', '--interactive', action='store_true', dest='interactive', help='- interactive controll app')
    parser.add_argument('-add', action='store', dest='add', help='- add new note, example: -add "label note"')
    parser.add_argument('-r','--restore', action='store_true', dest='rest', help='- return(view) all notes')
    parser.add_argument('-rm', '--remove', action='store', dest='remove', help='- remove note, example: -rm "label note"')
    args = parser.parse_args()
    
    print(vars(args))
    param = vars(args)
    #if args.add != 'ADD':
    for name, value in (param.items()):
        print(name, value)   
    if len(args_def) == 1:
        end_using = True
        while not end_using:
            
            end_using = controller.main()
            
            pass
    elif param['add'] != None:
        head = param['add']
        print("Enter/Paste your note. Ctrl-D or Ctrl-Z ( windows ) to save it.")
        contents = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
        note = single_note(datetime.utcnow(), head, '\n'.join(contents))
         
        controller.add_note(note)
        
    


if __name__ == '__main__':
    main()



