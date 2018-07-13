

# -*- coding: utf-8 -*-




"""Main module."""

"""
    Created on Wed Jul  4 17:03:14 2018
    
    @author: tfalcoff
"""



from .utils import sec_forms

class stock(object):
    
    
    def __init__(self, ticker):
        
        self.__ticker = ticker
        
    
    def __repr__(self):
        
        return '<stock {ticker}>'.format(ticker=self.__ticker)
    
    
    def get_ticker(self):
        
        return self.__ticker
    
    
    def set_ticker(self, ticker):
        
        self.__ticker = ticker
        
        
    def tenk_links(self, start_date, end_date):
        
        form = sec_forms(self.__ticker, form_type="10-K", start_date=start_date, end_date=end_date)

        return form.links
    
    
    def tenq_links(self, start_date, end_date):
        
        form = sec_forms(self.__ticker, form_type="10-Q", start_date=start_date, end_date=end_date)
        
        return form.links
    
    
    def tenk_IS(self, start_date, end_date):
        
        form = sec_forms(self.__ticker, form_type="10-K", start_date=start_date, end_date=end_date)
        
        return form.recentIS()

    
    def tenq_IS(self, start_date, end_date):   
        
        form = sec_forms(self.__ticker, form_type="10-Q", start_date=start_date, end_date=end_date)
        
        return form.recentIS()









