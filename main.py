import os.path
from FileAnalyzer import FileAnalyzer

# Global variables representing single line and block comments
SUPPORTED_EXTENSIONS = {".py": ("#" , "'''", "'''"), 
                        ".java": ("//", "/*", "*/"), 
                        ".tsx": ("//", "/*", "*/")}

# extension is a string,
def set_globals(extension):
    if extension not in SUPPORTED_EXTENSIONS:
        raise NotImplementedError
    else:
        return SUPPORTED_EXTENSIONS[extension]



# Get filename and file type of valid input, raise Error otherwise
def get_args():
    # Get absolute path of file
    file_abs_path = input("Enter the absolute path for the file: ")
    
    # Check if file is indeed a file
    if os.path.isfile(file_abs_path):
        filename, file_extension = os.path.splitext(file_abs_path)
        return filename, file_extension
    else:
        raise FileNotFoundError





def main():
    # Get file
    try:
        filename, file_extension = get_args()
    except:
        print("-------------ERROR!------------------")
        print("File is non valid, please enter a valid file")
        print("-------------------------------------")       
        return

    # Check if file extension is supported
    try:
        single_line_comment, block_line_comment_open, block_line_comment_close = set_globals(file_extension)
    except:
        print("-------------ERROR!------------------")
        print("Support for {} files have not been implemented".format(file_extension))
        print("-------------------------------------")
        return      

    file =  open(filename + file_extension, 'r')
    file_analyzer = FileAnalyzer(single_line_comment, block_line_comment_open, block_line_comment_close)
    
    file_analyzer.analyze(file)
    file_analyzer.get_results()


if __name__ == '__main__':
    main()



