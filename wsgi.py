import sys
from hvsi.wsgi import *
if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == 'debug':
		from bottle import run
		run(application, port=9055)
	else:
		from flup.server.fcgi import WSGIServer
		WSGIServer(application).run()
