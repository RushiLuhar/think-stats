'''
Created on Jun 17, 2012

@author: rushi
'''
import os
from decimal import *
from datetime import datetime

class OHLCRecord(object):
    '''
    Object contains details of the Open, High, Low, and Average closing price for a 
    paticular Date. 
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
class OHLCRecordCreator(object):
    
    def ReadFile(self, filename, datadir):
        # First create the appropriate operating system path for the file
        filename = os.path.join(datadir, filename)
        print 'Will read file: ', filename
        fields = self.GetFields()
        print 'Record fields: ', fields    
        # Try opening the file
        fh = open(filename)
        lineIdx = 0
        
        for line in fh.readlines():
            if (lineIdx == 0):
                pass
            else:
                print getattr(self.CreateRecord(fields, line),'date')
            lineIdx += 1
            if (lineIdx == 10): break
            
        fh.close()
        print 'Completed Reading File: ', filename
        
        
    def CreateRecord(self, fields, data):
        # Data is a comma delimited list of strings. Split the data First
        dataList = data.split(',')
        if (len(dataList) == len(fields)):
            ohlc_record = OHLCRecord()
            for field in fields:
                if (field[0] == 'date'):
                    setattr(ohlc_record, field[0], self.GetDate(dataList[field[1]]))
                else:
                    ''' Decimal class in python is safe representation of a floating point number 
                        with arbitrary precision which is set to 28 decimal places by default
                    '''
                    setattr(ohlc_record, field[0], Decimal(field[1]))
            return ohlc_record
        else:
            print 'Mismatch between data list size: ', dataList, " and field size: ", fields
        
        return None
    
    
    def GetDate(self, date_string):
        return datetime.strptime(date_string,'%Y-%m-%d')
    
    
    def GetFields(self):
        return [('date', 0),
                ('open',1),
                ('high',2),
                ('low',3),
                ('close',4),
                ('volume',5),
                ('adj_close',6)]
      
    
    def __init__(self):
        ''' Constructor '''

if __name__ == '__main__':
    ohlc_creator =  OHLCRecordCreator()
    ohlc_creator.ReadFile('VIX.csv', '../data')
    