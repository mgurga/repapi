# repapi
Simple JSON API to extract, parse, and host the US Representative website

## What data does this provide
- state's districts
- district number
- district party
- district offfice room
- district phone number
- district assignments
- lists zipcodes and their districts 

## How to access data
All the API endpoints return JSON

```http://apihost/```
- This will return a json formatted list of every state and their districts, very inefficent and returns ~500 kB of data

```http://apihost/state/[insert state here]```
- This will return the districts of the inputted state
- state name examples: "Texas", "PuertoRico", "AmericanSamoa". Some territories are counted as states

```http://apihost/stateabbr/[insert state abbr here]```
- This does the same as the above but uses state abbreviations
- state abbreviation examples: "TX", "PR", "AS"

```http://apihost/statelist```
- This returns a list of state names and their abbreviations that are used by the API

## How to compile data and host
You must have python3 and pip3 installed to compile the data
```
git clone https://github.com/mgurga/repapi
cd repapi
pip3 install -r requirements.txt
python3 extractor.py
python3 api.py
```
```extractor.py``` gets the data from the government website and puts it into json format


```api.py``` hosts a web server that returns the json values, uses port 8080 by default
