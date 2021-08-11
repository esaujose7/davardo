# TIC TAC TOE

## Requirements

* Python 3.7 or greater
* Python virtualenv

## Setup

1. Create a virtual environment

Linux:
```bash
// Linux
python3 -m venv venv

// Windows
py -3 -m venv venv
```

2. Activate the virtual environment

```bash
. venv/bin/activate
venv\Scripts\activate
```

3. Install the dependencies listed

```bash
pip install -r requirements.txt 
```

4. Start up the server

With all of these in place, you should be able to start up the development server without much issue with:
```bash
flask run
```

The entrypoint for the server is the `app.py` file, so check that out if you have any concern on the start up of the server.

Would say main dependency is [flask](https://flask.palletsprojects.com), so take a look as well at that if you have any question.