import sys
from data_service import Valid_Transaction_Filter_Service
from streaming_percentile import PercentileCalculator

class Percentile_Calculation_Service(object):
    """docstring for Donation_Analytics_Service."""
    def __init__(self, percentile):
        super(Percentile_Calculation_Service, self).__init__()
        self.percentile = percentile
        self.repeat_donors = {}
        self.percentile_map = {}

    def isRepeatContributer(self, transaction):
        donor_id = (transaction['ZIP_CODE'],transaction['NAME'])
        if donor_id in self.repeat_donors.keys():
            if self.repeat_donors[donor_id] <= transaction['TRANSACTION_DT']:
                return True
            else:
                #Ignore the transaction for the repeated donor
                return False
        else:
            #Add new Repeat donor
            self.repeat_donors[donor_id] = transaction['TRANSACTION_DT']
            return False

    def register(self, transaction):
        transaction_id = (transaction['TRANSACTION_DT'], transaction['ZIP_CODE'], transaction['CMTE_ID'] )
        if transaction_id not in self.percentile_map.keys():
            self.percentile_map[transaction_id] = PercentileCalculator(self.percentile)
        percentile_calculator = self.percentile_map[transaction_id]
        return percentile_calculator.add(transaction)




def main():
    input_filename, percentile_filename, output_filename = sys.argv[1:4]

    #Read percentile file and initiate the service
    with open(percentile_filename) as percentile_file:
        line =  percentile_file.readline()
        perc =  int(line)
        # NOTE: Percentile are assumed to be int. This can however be changed at a later stage

    vtfs = Valid_Transaction_Filter_Service()
    pcs = Percentile_Calculation_Service(perc)

    with open(input_filename) as ifp:
        with open(output_filename,'w') as ofp:
            for line in ifp:

                #Parse Line and check if the Record is valid
                transaction = vtfs.parse_line(line)
                result = None
                if vtfs.isValid(transaction):
                    #check if repeat donor and add record to register percentile
                    transaction = vtfs.transform(transaction)
                    if pcs.isRepeatContributer(transaction):
                        result = pcs.register(transaction)

                #Write the response to output file
                if result:
                    response = vtfs.delimiter.join(str(elem) for elem in result)
                    ofp.write(response)
                    ofp.write("\n")


if __name__ == "__main__":
    main()
'''
Test Cases to write for this file/class:
    Invalid Filenames
    Percentile file is empty
    Percentile File contains not an Integer value.
    Donation Analytics Service constructor is passed an empty arguements. ie: Percentile value is not mentioned.
'''
