
## Major Services
### Valid Transaction Filter Services
+ Currently takes in a line from the input file and parses it into appropriate transaction object.
+ Also filters out Invalid Line objects, return Null at the end of thee process(line) method.
+ Can be extended to accept other formats/objects directly.
+ Relies on ./input/indiv_header_file.csv for header definitions

### Repeat_Donor_Indentification_Service
+ Simple Hashset that returns True if the donor is repeat_donor.
+ Size: O(n)
+ Time: Constant-time lookup
Can be replaced by bloom filter if the files get too large.

## Percentile_Calculation_Service
+ Maintains a simple HashMap or Dictionary with: key-> Year,Zipcode,Candidate;  value -> Percentile_Calculator

### Percentile_Calculator:
+ Running Percentile Calculator using Nearest Rank method
+ Uses 2 heaps, Max-heap and min-heap internally.
+ Max-heap is limited to a size of total number of elements in both heaps combined.
+ Space: O(n)
+ Time: Insertion: O(log n)
+ Percentile Query fetch is Constant-time lookup since it is max-heap.base
