'''
Created on Jul 1, 2012

@author: rushi
'''

class _DictWrapper(object):
    
    def __init__(self, d = None, name = ''):
        if d == None:
            d = {}
        self.d = d
        self.name = name
    
    def get_dict(self):
        return self.d
    
    def set_value(self, x, y=0):
        self.d[x] = y
        
    def increment(self, x, term=1):
        self.d[x] = self.d.get(x, 0) + term
    
    def multiply(self, x, factor=1):
        self.d[x] = self.d.get(x, 0) * factor
        
    def remove(self, x):
        del self.d[x]
    
    def print_all(self):
        for key,value in sorted(self.d.iteritems()):
            print key, value
    
    def total(self):
        return sum(self.d.itervalues())
            
    def render(self):
        return zip(*sorted(self.d.items()))
    
    
class Histogram(_DictWrapper):
        
    def hist_values(self):
        return self.d.keys()
    
    def hist_items(self):
        return self.d.items()
    
    def get_freq(self, x):
        return self.d[x]
    
    def get_all_freqs(self):
        return self.d.values()
    
    def max_freq(self):
        return max(self.d.itervalues())
    
    def generate_from_list(self, l):
        [self.increment(x) for x in l]
    
    def generate_pmf(self):
        pmf = {}
        n = float(sum(self.get_all_freqs()))
        for x, freq in self.hist_items():
            pmf[x] = freq / n
        return pmf
            
class PMF(_DictWrapper):
    def generate_from_tuples(self, l):
                

def generate_histogram(l):
    h =  Histogram()
    h.generate_from_list(l)
    return h  