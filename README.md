# Apache `access.log` analyser CLI

This is a CLI to parse Apache `access.log` and return statistics like

1. Total number of request
2. Total number of successful requests
3. Top hosts making request

It is based on python3

## Requirements

- python >= 3.6

## CLI Options

The syntax to run the command is:

```bash
$ python3 main.py -h
usage: main.py [-h] [-t <count>] [-ts <count>] [-tf <count>] [-ps] [-pf] [-host <count>] <log file>

Apache log parser

positional arguments:
  <log file>     Name of the file to parse

optional arguments:
  -h, --help     show this help message and exit
  -t <count>     List top requested pages and their count
  -ts <count>    List top successful requests and their count
  -tf <count>    List top failed requests and their count
  -ps            Display percentage of successful requests
  -pf            Display percentage of failed requests
  -host <count>  List hosts with top number of requests
```

### `-t <count>`

List top requested pages or URI, along with their respective counts

```bash
$ python3 main.py -t 5 sample.log
Top 5 requested pages
*********************
1. "/apache-log/access.log": 2
2. "/favicon.ico": 2
3. "/robots.txt": 2
4. "/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53": 1
5. "/index.php?option=com_phocagallery&view=category&id=2%3Awinterfotos&Itemid=53": 1
```

### `-ts <count>`

List top sucessful requested pages or URI, along with their respective counts

```bash
$ python3 main.py -ts 5 sample.log
Top 5 successful page requests
******************************
1. "/apache-log/access.log": 2
2. "/robots.txt": 2
3. "/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53": 1
4. "/index.php?option=com_phocagallery&view=category&id=2%3Awinterfotos&Itemid=53": 1
5. "/administrator/index.php": 1
```

### `-tf <count>`

List top unsucessful/failed pages or URI, along with their respective counts

```bash
$ python3 main.py -tf 5 sample.log
Top 5 unsuccessful/failed page requests
***************************************
1. "/index.php?option=com_easyblog&view=dashboard&layout=write": 21
2. "/templates/_system/css/general.css": 19
3. "/favicon.ico": 7
4. "/index.php?option=com_contact&view=contact&id=1": 3
5. "/administrator/index.php": 3
```

### `-ps`

Shows the percentage of successful requests

```bash
$ python3 main.py -ps sample.log
Overall Successful requests: 77.78%
```

### `-pf`

Shows the percentage of unsuccessful/failed requests

```bash
$ python3 main.py -pf sample.log
Overall Failed requests: 22.22%
```

### `-host <count>`

List top <count> hosts along with the number of request initiated from them. Top 5 URI's from each host is also displayed.

```bash
$ python3 main.py -host 3  sample.log
Top 3 host requests
*******************
1. "10.11.12.13": 2
2. "173.0.162.225": 2
3. "192.168.139.101": 1

-------------Top 5 URI from each host-------------
10.11.12.13
***********
1. "/apache-log/access.log": 1
2. "/favicon.ico": 1

173.0.162.225
*************
1. "/apache-log/access.log": 1
2. "/favicon.ico": 1

192.168.139.101
***************
1. "/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53": 1
```

## Test Case

To execute the test cases, run:

```bash
$ python3 -m unittest discover
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
