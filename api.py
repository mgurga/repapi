import json
import cherrypy

repdata = None

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
			return repdata[state]["districts"]

cherrypy.quickstart(RepAPI())