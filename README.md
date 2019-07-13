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


A successful Playbook run should look like this:

```ansible

root@e7f1182cde2c:/ansible/Decomposing_DataStructures# ansible-playbook ios_facts_lab.yml
[DEPRECATION WARNING]: [defaults]hostfile option, The key is misleading as it can also be a list of hosts, a directory or a
 list of paths , use [defaults] inventory=/path/to/file|dir instead. This feature will be removed in version 2.8.
Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.

PLAY [Collect device facts with the ios_facts module and display selected values] ******************************************

TASK [Gather Facts with the facts module] **********************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output": {
        "ansible_facts": {
            "ansible_net_all_ipv4_addresses": [],
            "ansible_net_all_ipv6_addresses": [],
            "ansible_net_config": "socket_path does not exist or cannot be found. Please check https://docs.ansible.com/ansible/latest/network/user_guide/network_debug_troubleshooting.html#category-socket-path-issue",
            "ansible_net_filesystems": [
                "bootflash:"
            ],
            "ansible_net_gather_subset": [
                "hardware",
                "default",
                "interfaces",
                "config"
            ],
            "ansible_net_hostname": null,
            "ansible_net_image": null,
            "ansible_net_interfaces": {
                "socket_path": {
                    "bandwidth": null,
                    "description": null,
                    "duplex": null,
                    "ipv4": [],
                    "ipv6": [],
                    "lineprotocol": null,
                    "macaddress": null,
                    "mediatype": null,
                    "mtu": null,
                    "operstatus": null,
                    "type": null
                }
            },
            "ansible_net_memfree_mb": 2040749,
            "ansible_net_memtotal_mb": 2396128,
            "ansible_net_model": null,
            "ansible_net_neighbors": {
                "null": [
                    {
                        "host": null,
                        "port": null
                    }
                ]
            },
            "ansible_net_serialnum": null,
            "ansible_net_version": null
        },
        "changed": false,
        "failed": false
    }
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_hostname": ""
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_version": ""
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_model": ""
}

TASK [Display debug module msg with all variables of interest] *************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "msg": "Device with hostname  is of model type  running software version "
}

PLAY RECAP *****************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=6    changed=0    unreachable=0    failed=0

root@e7f1182cde2c:/ansible/Decomposing_DataStructures#

```