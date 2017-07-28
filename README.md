# Night Owls Detector

This script will detect a night owls within a [devman](http://devman.org) community. 

To do this it will connect to [devman api](http://devman.org/api/challenges/solution_attempts/?page=2), parse it, convert server local timezone to submitter local timezone and print out only late night submits.

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
pinguine сдал работу в 07:54
tonyflex сдал работу в 07:51
tonyflex сдал работу в 07:34
pinguine сдал работу в 07:08
tonyflex сдал работу в 06:49
id181118707 сдал работу в 02:06
tonyflex сдал работу в 00:53
tonyflex сдал работу в 05:28
ДмитрийВоронов сдал работу в 05:20
id54808965 сдал работу в 03:55
pinguine сдал работу в 07:25
tonyflex сдал работу в 05:06
pinguine сдал работу в 07:33
СергейИванов сдал работу в 07:01
tonyflex сдал работу в 05:56
ДмитрийВоронов сдал работу в 05:53
maksim.artemyev сдал работу в 05:45
maksim.artemyev сдал работу в 04:19
id240095620 сдал работу в 02:07
tonyflex сдал работу в 07:30
tonyflex сдал работу в 02:09
tonyflex сдал работу в 01:48
tonyflex сдал работу в 01:47
tonyflex сдал работу в 01:39
tonyflex сдал работу в 01:18
id290437617 сдал работу в 00:04
galbator1x сдал работу в 03:33
maksim.artemyev сдал работу в 07:56
pythoneyron сдал работу в 06:46
ДмитрийВоронов сдал работу в 06:10
ДмитрийВоронов сдал работу в 05:20
galbator1x сдал работу в 05:50
rs.porosenok сдал работу в 00:16
rs.porosenok сдал работу в 00:03
tonyflex сдал работу в 05:28
piterskikhsa сдал работу в 01:51
tonyflex сдал работу в 01:13
tonyflex сдал работу в 02:44
tonyflex сдал работу в 01:30
pinguine сдал работу в 00:22
pinguine сдал работу в 00:13
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
