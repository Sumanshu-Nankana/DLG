# Direct Line Group 

> Assignment Submitted By: Sumanshu Nankana
> Email : sumanshunankana@gmail.com
> Submission Date : 1st August 2021
--------------------------------------------------------------------------------
# Problem Statement
> Create a Rest endpoint which returns sum of list of integers
in json format

## How to Run
> On Linux Machine

Issue all commands on 'Terminal'. 
First redirect to the location where code.zip file is downloaded, then
issue below commands.

```sh
unzip code.zip
pip3 install -r requirements.txt
python3 app.py
curl localhost:5000/total        # output will be sum of first 1 to 10000000 numbers
curl localhost:5000/total/n      # where n could be any positive integer
                                 # output will be sum from 1 to n
```
Note:  list(range(10000001) is hardcoded in code

## How to Run Test Cases
```sh
unzip code.zip
pip3 install -r requirements.txt
python3 app.py
python3 -m pytest -v
```

> On Windows Machine

```sh
manually unzip the project.zip folder
pip install -r requirements.txt
python app.py
curl localhost:5000/total
curl localhost:5000/total/n      # where n could be any positive integer
```

## How to Run Test Cases
```sh
manually unzip the project.zip folder
pip install -r requirements.txt
python app.py
python -m pytest -v
```
