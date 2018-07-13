#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:03:14 2018

@author: tfalcoff
"""

import requests, regex, math

from bs4 import BeautifulSoup


class sec_forms(object):
    

    def __init__(self, stock, form_type="10-q", start_date="YYYY-MM-DD", end_date="YYYY-MM-DD"):

        self.__stock = stock

        self.__form_type = form_type

        self.__start_date = start_date

        self.__end_date = end_date

        self.__priming = self.__form_count_calc(form_type, str(start_date), str(end_date))

        self.links = self.__get_form(stock, form_type, self.__priming['priorto'])[:self.__priming['form_count']]


    def __form_count_calc(self, form_type, start_date, end_date):

        start = []

        [start.append(int(denom)) for denom in start_date.split("-")]

        end = []

        [end.append(int(denom)) for denom in end_date.split("-")]

        month_dif = (end[0]*12+end[1]) - (start[0]*12+start[1])

        if form_type.upper() == "10-Q":

            form_count = month_dif//4

        if form_type.upper() == "10-K":

            if (month_dif/12 - month_dif//12) >= .25:
                
                form_count = math.ceil(month_dif/12)
                
            else:

                form_count = month_dif//12

        priorto = end_date.replace("-","")
        
        return {"form_count":form_count, "priorto":priorto}


    def __get_form(self, ticker, form_type, priorto=""):

        base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+ticker+"&type="+form_type+"&dateb="+priorto+"&owner=exclude&count=40"        

        r = requests.get(base_url, timeout=.5)

        soup = BeautifulSoup(r.text, "html.parser")

        doc_buttons = soup.find_all(id="documentsbutton")
        
        links = []
        
        for button in doc_buttons:
            
            links.append(button.get("href"))

        form_links = []

        anchor = None

        for l in links:

            r2 = requests.get("https://www.sec.gov"+l, timeout=.5)

            soup2 = BeautifulSoup(r2.text, "html.parser")

            if form_type == "10-Q":

                anchor = soup2.find("a",string=regex.compile("q.htm"))

                if anchor == None:

                    anchor = soup2.find("a",string=regex.compile("10-q.htm"))

            if form_type == "10-K":

                anchor = soup2.find("a",string=regex.compile("k.htm"))

                if anchor == None:

                    anchor = soup2.find("a",string=regex.compile("10-k.htm"))
                    
            if anchor != None:

                form_links.append("https://www.sec.gov"+anchor.get("href"))

        return form_links
    

    def recentIS(self):

        text = ["income", "total", "net"]

        table = "After battling the interweb... it won d[-_-]b"

        try:

            r = requests.get(self.links[0], timeout=1)

            soup = BeautifulSoup(r.text,'html.parser')

            for t in soup.find_all('table'):

                txtCount = 0

                for txt in text:

                    if txt in str(t).lower() and len(t) < 100000:

                        txtCount += 1

                if txtCount == len(text):

                    table = str(t).replace("\n"," ")

                    table += "<br><br>"

                    break

        except:
            
            pass

        return table

