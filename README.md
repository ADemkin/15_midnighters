# Night Owls Detector

This script will detect a night owls within a [devman](http://devman.org) community. 

To do this it will connect to [devman api](http://devman.org/api/challenges/solution_attempts/?page=1), parse it, convert server local timezone to submitter local timezone and print out only late night submits.

# Installation
Script requires Python 3. To install additional modules run this terminal command from folder with this script:
```
pip3 install -r requirements.txt
```

# How to use

Simply run this script with terminal. No arguments required.
```
python3 seek_dev_nighters.py
```
Output example:
```
seek_dev_nighters.py
Ищем сов...
Вот они, наши совы:
galbator1x
tonyflex
maksim.artemyev
piterskikhsa
pinguine
ДмитрийВоронов
СергейИванов
pythoneyron
rs.porosenok
DmitriiSokolov
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
