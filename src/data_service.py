class Valid_Transaction_Filter_Service(object):
    """docstring for Valid_Transaction_Filter_Service."""
    def __init__(self, delimiter="|", header_file='./input/indiv_header_file.csv'):
        super(Valid_Transaction_Filter_Service, self).__init__()
        self.delimiter = delimiter
        self.header_file = header_file

        with open(self.header_file) as hfp:
            self.header = hfp.readline().split(",")

        self.essential_columns = ["CMTE_ID","NAME","ZIP_CODE","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID"]

    def parse_line(self,line):
        dictionary = dict( zip( self.header,line.split(self.delimiter) ) )
        #Filter non-essential columns. Not essential, but this can reduce data-transmitted across for later stages if needed.
        dictionary = {k:v for k,v in dictionary.items() if k in self.essential_columns}
        return dictionary

    def isValid(self,dictionary):
        # NOTE: We Hard-code this logic but can be latter changed if things get more complex later

        #If not an individual contributor, filter out
        if dictionary[self.essential_columns[5]]!='':
            return False

        #If any of the essential fields are empty, filter out
        for col in self.essential_columns[:5]:
            if dictionary[col]=='':
                return False

        return True

    '''
    TestCases:
        When header_file doesnot exist
        When empty header_file is passed
        Delimiter mismatches
        Parsing Empty line
        Essential Columns misspecification
    '''
