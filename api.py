import json
import cherrypy

repdata = None

with open("data.json", "r") as f:
	repdata = json.load(f)

class RepAPI:

	@cherrypy.tools.accept(media='application/json')

	@cherrypy.expose
	def index(self):
		return json.dumps(repdata)
	
	@cherrypy.expose
	def state(self, state):
		if state not in repdata:
			return "state does not exist"
		else:
			return json.dumps(repdata[state]["districts"])

cherrypy.quickstart(RepAPI())