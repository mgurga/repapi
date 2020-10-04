# repapi
Simple api to extract and parse the US Representative website

## What does this provide
- state's districts
- district number
- district party
- district offfice room
- district phone number
- district assignments

## How to access data
```http://apihost/```
- This will return a json formatted list of every state and their districts, very inefficent and returns ~75 kB of data

```http://apihost/state/[insert state here]```
- This will return the districts of the inputted state
- state name examples: "Texas", "PuertoRico", "AmericanSamoa". Some territories are counted as states

## How to compile data and host
You must have python3 and pip3 installed to compile the data
```
git clone https://github.com/rokie95/repapi
cd repapi
pip3 install -r requirements.txt
python3 extractor.py
python3 api.py
```
```extractor.py``` gets the data from the government website and puts it into json format


```api.py``` hosts a web server that returns the json values, uses port 8080
