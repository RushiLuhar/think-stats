'''
Created on Jun 18, 2012

@author: rushi
'''
from decimal import *

def calculate_variance(records, field):
    mean = calculate_mean(records, field)
    dev2 = [(getattr(record,field) - mean)**2 for record in records]
    return simple_mean(dev2)

def simple_mean(entries):
    return Decimal(sum(entries) / len(entries))

''' Calculates mean of a list of records for the value of a particular field '''
def calculate_mean(records, field): 
    if ( field != 'date'):
        running_total = Decimal(0)
        for record in records:
            try:
                running_total += getattr(record, field)
            except:
                print 'Error while trying to retrieve field: ', field
                break
        return running_total / Decimal(len(records))
    else:
        print 'Cannot calculate an average for the date field'


if __name__ == '__main__':
    pass