'''
Created on Jun 18, 2012

@author: rushi
'''
import OHLCRecord

def loadFiles(filename, filepath):
    try:
        ohlc_creator =  OHLCRecord.OHLCRecordCreator()
        ohlc_creator.ReadFile(filename, filepath)
        return ohlc_creator
    except:
        print 'Error while attempting to open file: ', filename
        
if __name__ == '__main__':
    print 'Starting Data analysis Sandbox'
    ohcl_records = loadFiles('VIX.csv', '../../data')