import json
import cherrypy

repdata = None
stateabbrlist = [
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

with open("data.json", "r") as f:
	repdata = json.load(f)

class RepAPI:

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self):
		return repdata
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def state(self, state):
		if state not in repdata:
			return "state does not exist"
		else:
			return repdata[state]
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def stateabbr(self, stateabbr):
		for i in stateabbrlist:
			if i[1] == stateabbr:
				return self.state(i[0])

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def statelist(self):
		return stateabbrlist

cherrypy.quickstart(RepAPI())