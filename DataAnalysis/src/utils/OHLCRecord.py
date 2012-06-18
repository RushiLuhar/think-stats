'''
Created on Jun 17, 2012

@author: rushi
'''
import os
from datetime import datetime
from decimal import *

class OHLCRecord(object):
    '''
    Object contains details of the Open, High, Low, Close and Adjusted Closing price for a 
    particular Date. 
    '''
    def __str__(self):
        return 'Symbol: '+self.symbol+' Date: '+str(self.date)+' Open: '+str(self.open)+\
            ' High: '+str(self.high)+' Low: '+str(self.low)+' Close: '+str(self.close)+\
            ' Volume: '+str(self.volume)+' Adj. Close: '+ str(self.adj_close) 
    
    def __init__(self):
        self.symbol = 'default'
        self.date = datetime.strptime('1970-01-01','%Y-%m-%d')
        self.open = Decimal(0)
        self.high = Decimal(0)
        self.low = Decimal(0)
        self.close = Decimal(0)
        self.volume = Decimal(0)
        self.adj_close = Decimal(0)
                
class OHLCRecordCreator(object):
    
    def read_file(self, filename, datadir, symbol):
        # First create the appropriate operating system path for the file
        filename = os.path.join(datadir, filename)
        print 'Will read file: ', filename
        fields = self.get_fields()
        print 'Record fields: ', fields    
        # Try opening the file
        fh = open(filename)
        lineIdx = 0
        for line in fh.readlines():
            if (lineIdx == 0):
                pass
            else:
                self.add_record(self.create_record(fields, line, symbol))
            lineIdx += 1
        fh.close()
        # Sort the file by timestamp
        self.records.sort(key = lambda record: record.date)
        print 'Completed Reading File: ', filename
        print 'Total Number of records: ', len(self.records)
        
        
    def create_record(self, fields, data, symbol):
        # Data is a comma delimited list of strings. Split the data First
        dataList = data.split(',')
        if (len(dataList) == len(fields)):
            ohlc_record = OHLCRecord()
            for field in fields:
                if (field[0] == 'date'):
                    ohlc_record.date = self.get_date(dataList[field[1]])
                else:
                    setattr(ohlc_record, field[0], Decimal(dataList[field[1]]))
                ohlc_record.symbol = symbol
            return ohlc_record
        else:
            print 'Mismatch between data list size: ', dataList, " and field size: ", fields
        
        return None
    
    
    def get_date(self, date_string, date_format = '%Y-%m-%d'):
        return datetime.strptime( date_string, date_format )
    
    
    def get_fields(self):
        return [('date', 0),
                ('open',1),
                ('high',2),
                ('low',3),
                ('close',4),
                ('volume',5),
                ('adj_close',6)]
      
      
    def add_record(self, record):
        self.records.append(record)
    
    def get_records_inrange(self, start, end):
        start_date = self.get_date(start)
        end_date = self.get_date(end)
        if (start_date > end_date):
            temp = end_date
            end_date = start_date
            start_date = temp
        return [ record for record in self.records if (record.date >= start_date and record.date < end_date) ]     
    
    def __init__(self):
        ''' Constructor '''
        # Define the internal records field that will store all recorgds
        self.records = []


if __name__ == '__main__':
    ohlc_creator =  OHLCRecordCreator()
    ohlc_creator.read_file('VIX.csv', '../data','VIX')
    