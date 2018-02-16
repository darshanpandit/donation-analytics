import sys
from data_service import Valid_Transaction_Filter_Service

class Donation_Analytics_Service(object):
    """docstring for Donation_Analytics_Service."""
    def __init__(self, percentile):
        super(Donation_Analytics_Service, self).__init__()
        self.percentile = percentile

    def register_contribution(self):
        return None;




def main():
    input_filename, percentile_filename, output_filename = sys.argv[1:4]

    #Read percentile file and initiate the service
    with open(percentile_filename) as percentile_file:
        line =  percentile_file.readline()
        perc =  int(line)
        # NOTE: Percentile are assumed to be int. This can however be changed at a later stage

    donation_analytics_service = Donation_Analytics_Service(perc)
    vtfs = Valid_Transaction_Filter_Service()


    with open(input_filename) as ifp:
        with open(output_filename,'w') as ofp:
            for line in ifp:

                #Parse Line and check if the Record is valid
                temp = vtfs.parse_line(line)
                vtfs.isValid(temp)

                

                #Write the response to output file
                ofp.write(str(vtfs.isValid(temp)))
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
