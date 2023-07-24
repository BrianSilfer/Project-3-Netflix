# Import Yahoo Finance and JSON Dependency 
import yfinance as yf
import json
#define variable to store Netflix stock data
nflx = yf.Ticker("NFLX")

#print results
#print(nflx.info)

#convert dictionary to JSON
nflx_json = json.dumps(nflx,indent = 4, sort_keys=True)
print(nflx_json)