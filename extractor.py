import urllib.request
import os
import json
import csv
from bs4 import BeautifulSoup


houserepwebsite = "https://www.house.gov/representatives"
uszipcodes = "https://raw.githubusercontent.com/OpenSourceActivismTech/us-zipcodes-congress/master/zccd.csv"


repjson = json.loads("{}")
zccsv = None
stateabbr = [
	["Alabama", "AL"],
	["Alaska", "AK"],
	["AmericanSamoa", "AS"],
	["Arizona", "AZ"],
	["Arkansas", "AR"],
	["California", "CA"],
	["Colorado", "CO"],
	["Connecticut", "CT"],
	["Delaware", "DE"],
	["DistrictofColumbia", "DC"],
	["Florida", "FL"],
	["Georgia", "GA"],
	["Guam", "GU"],
	["Hawaii", "HI"],
	["Idaho", "ID"],
	["Illinois", "IL"],
	["Indiana", "IN"],
	["Iowa", "IA"],
	["Kansas", "KS"],
	["Kentucky", "KY"],
	["Louisiana", "LA"],
	["Maine", "ME"],
	["Maryland", "MD"],
	["Massachusetts", "MA"],
	["Michigan", "MI"],
	["Minnesota", "MN"],
	["Mississippi", "MS"],
	["Missouri", "MO"],
	["Montana", "MT"],
	["Nebraska", "NE"],
	["Nevada", "NV"],
	["NewHampshire", "NH"],
	["NewJersey", "NJ"],
	["NewMexico", "NM"],
	["NewYork", "NY"],
	["NorthCarolina", "NC"],
	["NorthDakota", "ND"],
	["NorthernMarianaIslands", "NI"],
	["Ohio", "OH"],
	["Oklahoma", "OK"],
	["Oregon", "OR"],
	["Pennsylvania", "PA"],
	["PuertoRico", "PR"],
	["RhodeIsland", "RI"],
	["SouthCarolina", "SC"],
	["SouthDakota", "SD"],
	["Tennessee", "TN"],
	["Texas", "TX"],
	["Utah", "UT"],
	["Vermont", "VT"],
	["Virginia", "VA"],
	["VirginIslands", "VI"],
	["Washington", "WA"],
	["WestVirginia", "WV"],
	["Wisconsin", "WI"],
	["Wyoming", "WY"]
]

# create temp dir if not existing
if not os.path.exists("tmp"):
	os.mkdir("tmp")

print("downloading representatives website...")
urllib.request.urlretrieve(houserepwebsite, "tmp/reps.html")

print("downloading zip codes...")
urllib.request.urlretrieve(uszipcodes, "tmp/zccd.csv")

# parse rep website
print("loading html with beautifulsoup...")
repshtml = None
with open("tmp/reps.html", "r") as f:
	# print(f.read())
	repshtml = BeautifulSoup(f.read(), "html.parser")

def abbr2state(abbr):
	for i in stateabbr:
		if abbr == i[1]:
			return i[0]
	return "ERR"

# get all tables
souptables = repshtml.find_all("caption")[0:56]
# print(souptables)

def clean(data):
	return data.replace(" ", "").replace("\n", "")

# loop through all states in table
for state in souptables:
	statetable = state.parent
	statename = clean(state.text)
	statedistricts = statetable.find_all("tr")[1:]

	print("loaded state: " + statename)
	print("num of districs: " + str(len(statedistricts)))

	repjson[statename] = {}
	repjson[statename]["districts"] = []
	repjson[statename]["zipcodes"] = {}

	# loop through all districs in state
	for district in statedistricts:
		districtjson = json.loads("{}")

		districtrowdata = district.find_all("td")
		districtnum = clean(districtrowdata[0].text)
		districtname = clean(districtrowdata[1].find("a").text)
		districtparty = clean(districtrowdata[2].text)
		districtofficeroom = clean(districtrowdata[3].text)
		districtphone = clean(districtrowdata[4].text)
		districtassignlist = districtrowdata[5].find_all("li") # array of assignment
		districtassignraw = []
		districtassign = ""
		for a in districtassignlist:
			districtassignraw.append(a.text)
			if districtassign == "":
				districtassign = a.text
			else:
				districtassign = districtassign + "," + a.text

		sep = " | "
		# print(districtnum + sep + districtname + sep + districtparty + sep + districtofficeroom + sep + districtphone + sep + districtassign)

		districtjson["num"] = districtnum
		districtjson["name"] = districtname
		districtjson["party"] = districtparty
		districtjson["officeroom"] = districtofficeroom
		districtjson["phone"] = districtphone
		districtjson["assignments"] = districtassignraw

		repjson[statename]["districts"].append(districtjson)

	# print()

# load zip code csv
with open("tmp/zccd.csv") as f:
	zccsv = csv.reader(f)
	# for row in zccsv:
		# print(row)

	for row in zccsv:
		fullstatename = abbr2state(row[1])
		# print(fullstatename)

		if fullstatename != "ERR":
			repjson[fullstatename]["zipcodes"][row[2]] = str(row[3])

with open('data.json', 'w') as f:
	json.dump(repjson, f)
