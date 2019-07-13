## Decomposing Data Structures

This repository provides some basic examples and data used in my *Decomposing Data Structures* post on [The Gratuitous Arp](https://gratuitous-arp.net/decomposing-data-structures/).

In addition to examples of structured data (see the json and txt files) there are two example scripts available:

Script | Description
-------|------------------
country_info_rest.py | Python3 script to access REST Country API data and optionally decompose the returned data structure
ios_facts_lab.yml | Ansible playbook to gather facts from a DevNet Sandbox device and decompose the returned data structure


If you don't have an Ansible control host handy, try one of my Ansible Docker images.
Also, note that this repository has a very minimalistic Ansible environment defined via the included host and ansible.cfg files.
This playbook uses the Cisco DevNet IOS-XE Sandbox device and you may need to run it a few times for a response.

```
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