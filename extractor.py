import urllib
import os
import json
from bs4 import BeautifulSoup

repjson = json.loads("{}")

# create temp dir if not existing
if not os.path.exists("tmp"):
	os.mkdir("tmp")

print("downloading representatives website...")
urllib.request.urlretrieve("https://www.house.gov/representatives", "tmp/reps.html")

print("loading html with beautifulsoup...")
repshtml = None
with open("tmp/reps.html", "r") as f:
	# print(f.read())
	repshtml = BeautifulSoup(f.read(), "html.parser")

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

	print(statename)
	print("num of districs: " + str(len(statedistricts)))

	repjson[statename] = {}
	repjson[statename]["districts"] = []

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
		print(districtnum + sep + districtname + sep + districtparty + sep + districtofficeroom + sep + districtphone + sep + districtassign)

		districtjson["num"] = districtnum
		districtjson["name"] = districtname
		districtjson["party"] = districtparty
		districtjson["officeroom"] = districtofficeroom
		districtjson["phone"] = districtphone
		districtjson["assignments"] = districtassignraw

		repjson[statename]["districts"].append(districtjson)

	print()

with open('data.json', 'w') as f:
	json.dump(repjson, f)