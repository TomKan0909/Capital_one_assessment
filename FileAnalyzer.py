class FileAnalyzer:

    def __init__(self, single_line_comment, block_line_comment_open, block_line_comment_close):
        # File analyzer Variable
        self.lines = 0
        self.comment_lines = 0
        self.single_line_comments = 0
        self.lines_within_block = 0
        self.block_line_comments = 0
        self.TODO = 0;
        # Variables that represent comment type
        self.single_line_comment = single_line_comment
        self.block_line_comment_open = block_line_comment_open
        self.block_line_comment_close = block_line_comment_close





    # file is a file object from open() python call
    def analyze(self, file):
        file_lines = file.readlines()

        in_block = False
        # Iterate each line in file
        for l in file_lines:
            # check if line contains a comments
            if self._contain_comment(l, in_block):
                
                #single line comment case
                if self.single_line_comment in l:
                    self._handle_single_line(l)
                #block comment case
                else:
                    in_block = self._handle_block_comment(l, in_block)
                
                self.comment_lines += 1
            
        
            self.lines += 1
            


    def _handle_block_comment(self, file_line, in_block):
        if self.block_line_comment_open in file_line:
            in_block = True
            self.block_line_comments += 1
            # Check if block line comment close on same line
            if self.block_line_comment_close in file_line:
                in_block = False
        else: # inside a block comment that is not start
            if self.block_line_comment_close in file_line:
                in_block = False
        self.lines_within_block += 1
        return in_block

    
    def _handle_single_line(self, file_line):
        if 'TODO' in file_line:
            self.TODO += 1
        self.single_line_comments += 1

    def _contain_comment(self, file_line, in_block):
        return self.single_line_comment in file_line or self.block_line_comment_open in file_line or in_block


    # Call this method after analyze to get metedata of file
    def get_results(self):
        print("Total # of lines: {}".format(self.lines))
        print("Total # of comment lines: {}".format(self.comment_lines))
        print("Total # of single line comments: {}".format(self.single_line_comments))
        print("Total # of comment lines within block comments: {}".format(self.lines_within_block))
        print("Total # of block line comments: {}".format(self.block_line_comments))
        print("Total # of TODO's: {}".format(self.TODO))
        


    
