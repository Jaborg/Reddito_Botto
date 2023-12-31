setup:
	 python3 -m venv env
	 env/bin/python3 -m pip install --upgrade pip
	 env/bin/pip3 install -r requirements.txt

run_app:
	env/bin/python3 app/main.py

