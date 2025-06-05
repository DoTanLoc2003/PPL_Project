import sys, os
import subprocess
import unittest
import json
from antlr4 import *

DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'chatbox.g4'

def printUsage():
    print('python chatbox.py gen')
    print('python chatbox.py run')

def printBreak():
    print('-------------------------------------------------')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-visitor', '-no-listener', '-Dlanguage=Python3', SRC])

    print('Generate successfully.')
    
def run():
    print('Chatbox is now online! Please proceed the command or type \'exit\' to stop the chatbox.')
    
    from CompiledFiles.chatboxLexer import chatboxLexer
    from CompiledFiles.chatboxParser import chatboxParser
    from antlr4.error.ErrorListener import ErrorListener
    
    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)
    
    from CartVisitor import CartVisitor
    visitor = CartVisitor()

    while True:
        try:
            user_input = input("\n>> ").strip().lower()
            if not user_input:
                continue
            if user_input in ("exit", "quit"):
                print("Exiting chatbox.")
                break

            input_stream = InputStream(user_input)
            lexer = chatboxLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(CustomErrorListener())

            token_stream = CommonTokenStream(lexer)
            parser = chatboxParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(CustomErrorListener())

            tree = parser.program()
            result = visitor.visit(tree)

            if visitor.error:
                print(f"Error: {visitor.error}")
                visitor.error = None
            elif result is not None:
                print(result)

        except Exception as e:
            print(f"Input rejected: {e}")
  
def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'run':       
        run()
    else:
        printUsage()

if __name__ == "__main__":
    main(sys.argv[1:])

# noname4now