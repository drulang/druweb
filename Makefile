env:
	sudo easy_install pip && \
	pip install virtualenv && \
	virtualenv venv && \
	. venv/bin/activate && \
	make deps

deps:
	pip install -r requirements.txt
