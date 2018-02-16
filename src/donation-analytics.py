import sys

class Donation_Analytics_Service(object):
    """docstring for Donation_Analytics_Service."""
    def __init__(self, percentile):
        super(Donation_Analytics_Service, self).__init__()
        self.percentile = percentile

    def register_contribution():
        return None;



def main():
    input_filename, percentile_filename, output_filename = sys.argv[1:4]

    #Read percentile file and initiate the service
    with open(percentile_filename) as percentile_file:
        line =  percentile_file.readline()
        perc =  int(line)
        # NOTE: Percentile are assumed to be int. This can however be changed at a later stage

    donation_analytics_service = Donation_Analytics_Service(perc)

    with open(input_filename) as ifp:
        with open(output_filename,'w') as ofp:
            for line in ifp:
                print(line)
                ofp.write(line)


if __name__ == "__main__":
    main()
'''
Test Cases to write for this file/class:
    Invalid Filenames
    Percentile file is empty
    Percentile File contains not an Integer value.
    Donation Analytics Service constructor is passed an empty arguements. ie: Percentile value is not mentioned.
'''
