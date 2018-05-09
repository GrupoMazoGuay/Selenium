test: executeTests

executeTests:
	sh -c '. venv/bin/activate; nosetests tests'

bootstrap: venv
	venv/bin/pip install -e .
ifneq ($(wildcard requirements.txt),)
	venv/bin/pip install -r requirements.txt
endif

venv:
	virtualenv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools

startServer:
	cd www
	python -m SimpleHTTPServer 8080 &

stopServer:
	kill $(server.PID)


