# Learning Flask Web Development part 1

## Requirement 

- pyenv

## How to

1. clone this repository
```
git clone https://github.com/aysf/learn_flask_web_dev_1.git
```

2. Then change into the folder:
```
cd learn_flask_web_dev_1
```

3. ensure that your python version is same with `.python-version` file
```
python -V
```

4. create venv, activate it and install all the requirement packages
```
python -m venv venv
./venv/bin/activate
pip install -r requirements
```

5. export enviroment variable
```
export FLASK_APP=hello.py # on windows set FLASK_APP=hello.py
export FLASK_DEBUG=1  
```

6. run flask
```
flask run
```
