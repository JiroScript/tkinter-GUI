import time
import os
import sys

if sys.platform == 'win32':
    import win32api
    import win32print

class Printer:
    
    @staticmethod
    def post():
        path = Indexer.get_relative_path("/paper/")
        file_list = os.listdir(path)
        Printer.print_files(file_list, path)
        
    @staticmethod
    def print_files(file_list, path):
        for file_name in file_list:
            Printer.print_out(file_name, path)
        
    @staticmethod
    def print_out(file_name, path):
        if sys.platform != 'win32':
            print("This function can only be executed on Windows.")
            return
        
        win32api.ShellExecute(0, "print", file_name, '/c:"%s"' % win32print.GetDefaultPrinter(), path, 0)
        print('印刷が実行されました')
        time.sleep(1)
        
class Indexer:

    @staticmethod
    def get_relative_path(directory):
        current_path = os.getcwd()
        return os.path.relpath(directory, current_path)
    
if __name__ == '__main__':
    Printer.post()
