'''
Created on Jun 18, 2012

@author: rushi
'''
import OHLCRecord
import StatModules
import Histogram
import matplotlib.pyplot as pyplot

def load_files(filename, filepath, symbol):
    try:
        ohlc_creator = OHLCRecord.OHLCRecordCreator()
        ohlc_creator.read_file(filename, filepath, symbol)
        return ohlc_creator
    except:
        print 'Error while attempting to open file: ', filename
        
        
        
if __name__ == '__main__':
    print 'Starting Data analysis Sandbox'
    ohlc_records = load_files('VIX.csv', '../../data', 'VIX')
    filtered_records = ohlc_records.get_records_inrange('2012-01-01', '2012-06-15')
    print 'Variance High VIX 2012: ', StatModules.calculate_variance(filtered_records, 'high')
    print 'Standard Deviation VIX 2012: ', StatModules.calculate_stdev(filtered_records, 'high')
    h = Histogram.generate_histogram([1,2,3,3,3,5])
    vals, freqs = h.render()
    rectangles = pyplot.bar(vals, freqs)
    pyplot.show()
    '''
    print 'Average open: ', StatModules.calculate_mean(ohlc_records.records, 'open')
    print 'Average close: ', StatModules.calculate_mean(ohlc_records.records, 'close') 
    print 'Variance open: ', StatModules.calculate_variance(ohlc_records.records, 'open') '''
