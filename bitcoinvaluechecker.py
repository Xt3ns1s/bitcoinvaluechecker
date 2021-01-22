#python 3.8.6

#For this I hope I can successfully code a script that checkes the latest bitcoin value.

import requests
import subprocess

subprocess.run (["clear"])

print ("For checking the current value of bitcoin.")

r=requests.get ("https://api.coinbase.com/v2/prices/spot?currency=USD")

print (r.text)
