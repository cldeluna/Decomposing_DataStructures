## Decomposing Data Structures

This repository provides some basic examples and data used in my *Decomposing Data Structures* post on [The Gratuitous Arp](https://gratuitous-arp.net/decomposing-data-structures/).

In addition to examples of structured data (see the json and txt files) there are two example scripts available:

Script | Description
country_info_rest.py
ios_facts_lab.yml



```python
(gen_py3_env) Claudias-iMac:Decomposing_DataStructures claudia$ python country_info_rest.py -h
usage: country_info_rest.py [-h] [-n CNAME] [-d]

Call REST Countries REST API with a country name.

optional arguments:
  -h, --help            show this help message and exit
  -n CNAME, --cname CNAME
                        Country Name to override default (Mexico)
  -d, --decompose       Execute a function to help decompose the response

Usage: 'python country_info_rest.py' without the --cname argument the script
will use the default country name of Mexico. Usage with optional name
parameter: 'python country_info_rest.py -n Singapore'. Note: this is a python3
script.
(gen_py3_env) Claudias-iMac:Decomposing_DataStructures claudia$ 


```