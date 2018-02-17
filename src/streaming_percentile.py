from math import ceil
from heapq import heappush,nsmallest, heapreplace

#We use maintain 2 heaps, a max-heap whose size varies based upon the total elements and percentile; and an unrestricted min-heap.
#Using this we are able to get constant time percentile lookups and logarithmic insertions.

class PercentileCalculator(object):
    """docstring for PercentileCalculator."""
    def __init__(self, percentile):
        super(PercentileCalculator, self).__init__()
        self.min_heap = []
        self.max_heap = []
        self.max_heap_size = 0
        self.transaction_count = 0
        self.transaction_amount = 0
        self.percentile = percentile

    def update_max_heapsize(self):
        return round(self.percentile*self.transaction_count/100)


    def add(self, transaction):
        t_amnt = transaction['TRANSACTION_AMT']
        self.transaction_count = self.transaction_count + 1
        self.transaction_amount = self.transaction_amount + t_amnt
        self.update_max_heapsize()

        if len(self.max_heap) == 0:
            heappush(self.max_heap, -t_amnt)

        # if transaction amount is larger than percentile amount
        elif t_amnt > ( - nsmallest(1, self.max_heap)[0] ):
            heappush(self.min_heap,t_amnt)

        else:
            #We push Negative values to Max_heap since the underlying implementation is a min_heap. While retrieving values from the heap, we negate it as well.
            #If the Max Heap is not exhausted
            if len(self.max_heap) < self.max_heap_size:
                heappush(self.max_heap, -t_amnt)
            else:
                #If Max Heap is exhausted, ie: If there is going to be a change in Percentile value
                temp = heapreplace(self.max_heap,(-t_amnt))
                heappush(self.min_heap,(-temp))
        temp = - nsmallest(1,self.max_heap)[0]

        return [transaction['CMTE_ID'],transaction['ZIP_CODE'],transaction['TRANSACTION_DT'],round(temp),self.transaction_amount,self.transaction_count]
