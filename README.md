## Decomposing Data Structures

This repository provides some basic examples and data used in my *Decomposing Data Structures* post on [The Gratuitous Arp](https://gratuitous-arp.net/decomposing-data-structures/).

In addition to examples of structured data (see the json and txt files) there are two example scripts available:

Script | Description
-------|------------------
country_info_rest.py | Python3 script to access REST Country API data and optionally decompose the returned data structure
ios_facts_lab.yml | Ansible playbook to gather facts from a DevNet Sandbox device and decompose the returned data structure


If you don't have an Ansible control host handy, try one of my [Ansible Docker images](https://hub.docker.com/r/cldeluna/cosmic-light).
Also, note that this repository has a very minimalistic Ansible environment defined via the included hosts and ansible.cfg files.
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

root@07163e92ec9b:/ansible_local/Decomposing_DataStructures# ansible-playbook ios_facts_lab.yml
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
            "ansible_net_all_ipv4_addresses": [
                "192.168.50.1",
                "192.168.109.100",
                "10.10.20.48",
                "10.10.10.14",
                "192.168.128.2"
            ],
            "ansible_net_all_ipv6_addresses": [],
            "ansible_net_config": "Building configuration...\n\nCurrent configuration : 4674 bytes\n!\n! Last configuration change at 19:35:21 UTC Mon Jul 15 2019 by root\n!\nversion 16.8\nservice timestamps debug datetime msec\nservice timestamps log datetime msec\nplatform qfp utilization monitor load 80\nno platform punt-keepalive disable-kernel-core\nplatform console virtual\n!\nhostname csr1000v\n!\nboot-start-marker\nboot-end-marker\n!\n!\nno logging console\nenable secret 5 $1$8Cgp$pN3C9FxnFiQ7CnYpSk.5S.\n!\nno aaa new-model\n!\n!\n!\n!\n!\n!\n!\nno ip domain lookup\nip domain name abc.inc\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\nsubscriber templating\n! \n! \n! \n! \n!\n!\n!\nmultilink bundle-name authenticated\n!\n!\n!\n!\n!\ncrypto pki trustpoint TP-self-signed-3053958489\n enrollment selfsigned\n subject-name cn=IOS-Self-Signed-Certificate-3053958489\n revocation-check none\n rsakeypair TP-self-signed-3053958489\n!\n!\ncrypto pki certificate chain TP-self-signed-3053958489\n certificate self-signed 01\n  30820330 30820218 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 \n  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 \n  69666963 6174652D 33303533 39353834 3839301E 170D3138 30343035 31303437 \n  35355A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 \n  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 30353339 \n  35383438 39308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 \n  0A028201 0100B59A DFFA19DB B337FE58 876BEAC9 D081E33D 23D8150D B1851B7B \n  0FEE6418 4D343FFF 59BE723E 0184D95B FF362B69 10F885E3 C267CEA7 6B36A1B8 \n  07761438 FA92D320 9AD73CBD A650354E F5916E8A 21391DFA 44D5E412 79DFED6C \n  F7A9265D 1F026689 98978336 73B5E7EB 69EE1AEE 3F2870C8 30E1DEAE 6A3E3953 \n  767C401F 6FA5B2FF F4175B83 355BA87B 0BC3A48E EE7D4576 6464D69D 4CEED994 \n  F3ED8A8F 221928B5 D164626E 296BB25F 043CD904 8B176894 E9BADC26 BD2465C2 \n  778AA603 9E989FCF FA44AAF0 B7821BCA 120A010E D6DD591E 86A100F3 44010890 \n  8FD8CBE6 41916951 BCB025FF 7CD57408 323B6F96 94078048 12D78293 FD9467FA \n  E3A7E098 67F70203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF \n  301F0603 551D2304 18301680 1480D4D0 3385D853 C16C7F3A 4FAEA7A0 6C8CF63C \n  EC301D06 03551D0E 04160414 80D4D033 85D853C1 6C7F3A4F AEA7A06C 8CF63CEC \n  300D0609 2A864886 F70D0101 05050003 82010100 1FE4B312 E1B99657 1D4B6742 \n  84249592 8E6C724C 50854F77 74BA7FF5 EB68F547 7141412E BA9D211A 7D11E759 \n  4D70AB1E 6F3D79DF 4171E94E 851EA63A 8D32BE61 B6A77863 A5C3B20F DEE1B736 \n  66DC18EE B98BC754 4E431093 B2C318E2 CD01697E F88900E3 1A5430DF 4026C540 \n  E72F48C5 7D30000C 401B0420 C9E5E874 B68A8CCC C31033EE BC7C51FD 03D84BA8 \n  AF24C6CD FBCE9415 3124593F CF17E10B 833F978F BDE25166 8C3BAB1D 35F2731D \n  4DB92A3C 4EBB8E3E 8B76C84A 5BB73814 4C585C9C AC22C6E2 EFDDEEF7 02EEA3D0 \n  93DB6396 0A7EF2FA 766F7111 43AF8163 40348266 BEA8F96E 575EC5DE 02E58E0A \n  AA78608F 326452BE 4F584805 0C387ED5 4C0B99C7\n  \tquit\n!\n!\n!\n!\n!\n!\n!\n!\nlicense udi pid CSR1000V sn 9JGOSIUGQVN\nlicense accept end user agreement\nlicense boot level ax\nno license smart enable\ndiagnostic bootup level minimal\n!\nspanning-tree extend system-id\n!\nnetconf-yang\n!\nrestconf\n!\nusername cisco privilege 15 secret 5 $1$QaEp$bTeddcdYn1RZceLMVL6RC1\nusername root privilege 15 password 0 D_Vay!_10&\n!\nredundancy\n!\n!\n!\n!\n!\n!\n! \n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n! \n! \n!\n!\ninterface Loopback9\n description __TEST__ 9\n ip address 192.168.109.100 255.255.255.0\n!\ninterface Loopback30\n description NetConf Lab\n ip address 192.168.50.1 255.255.255.0\n!\ninterface GigabitEthernet1\n description DON'T TOUCH ME\n ip address 10.10.20.48 255.255.255.0\n negotiation auto\n no mop enabled\n no mop sysid\n!\ninterface GigabitEthernet2\n description Configured by NAN0\n ip address 10.10.10.14 255.255.255.0 secondary\n ip address 192.168.128.2 255.255.255.0\n negotiation auto\n no mop enabled\n no mop sysid\n!\ninterface GigabitEthernet3\n no ip address\n shutdown\n negotiation auto\n no mop enabled\n no mop sysid\n!\nip forward-protocol nd\nip http server\nip http authentication local\nip http secure-server\nip route 0.0.0.0 0.0.0.0 GigabitEthernet1 10.10.20.254\nip route 8.8.8.8 255.255.255.255 GigabitEthernet1 10.10.20.254\n!\nip ssh rsa keypair-name ssh-key\nip ssh version 2\nip scp server enable\n!\n!\n!\n!\n!\ncontrol-plane\n!\n!\n!\n!\n!\nbanner motd ^C\nWelcome to the DevNet Always On Sandbox for IOS XE\n\nThis is a shared sandbox available for anyone to use to\ntest APIs, explore features, and test scripts.  Please\nkeep this in mind as you use it, and respect others use.\n\nThe following programmability features are already enabled:\n  - NETCONF\n  - RESTCONF\n\nThanks for stopping by.\n^C\n!\nline con 0\n exec-timeout 0 0\n logging synchronous\n stopbits 1\nline vty 0 4\n login local\n transport input ssh\n!\nwsma agent exec\n!\nwsma agent config\n!\nwsma agent filesys\n!\nwsma agent notify\n!\n!\nend",
            "ansible_net_filesystems": [
                "bootflash:"
            ],
            "ansible_net_filesystems_info": {
                "bootflash:": {
                    "spacefree_kb": 6846844,
                    "spacetotal_kb": 7712692
                }
            },
            "ansible_net_gather_subset": [
                "hardware",
                "default",
                "interfaces",
                "config"
            ],
            "ansible_net_hostname": "csr1000v",
            "ansible_net_image": "bootflash:packages.conf",
            "ansible_net_interfaces": {
                "GigabitEthernet1": {
                    "bandwidth": 1000000,
                    "description": "DON'T TOUCH ME",
                    "duplex": "Full",
                    "ipv4": [
                        {
                            "address": "10.10.20.48",
                            "subnet": "24"
                        }
                    ],
                    "lineprotocol": "up ",
                    "macaddress": "0050.56bb.18c4",
                    "mediatype": "Virtual",
                    "mtu": 1500,
                    "operstatus": "up",
                    "type": "CSR vNIC"
                },
                "GigabitEthernet2": {
                    "bandwidth": 1000000,
                    "description": "Configured by NAN0",
                    "duplex": "Full",
                    "ipv4": [
                        {
                            "address": "10.10.10.14",
                            "subnet": "24"
                        },
                        {
                            "address": "192.168.128.2",
                            "subnet": "24"
                        }
                    ],
                    "lineprotocol": "up ",
                    "macaddress": "0050.56bb.ac30",
                    "mediatype": "Virtual",
                    "mtu": 1500,
                    "operstatus": "up",
                    "type": "CSR vNIC"
                },
                "GigabitEthernet3": {
                    "bandwidth": 1000000,
                    "description": null,
                    "duplex": "Full",
                    "ipv4": [],
                    "lineprotocol": "down ",
                    "macaddress": "0050.56bb.1669",
                    "mediatype": "Virtual",
                    "mtu": 1500,
                    "operstatus": "administratively down",
                    "type": "CSR vNIC"
                },
                "Loopback30": {
                    "bandwidth": 8000000,
                    "description": "NetConf Lab",
                    "duplex": null,
                    "ipv4": [
                        {
                            "address": "192.168.50.1",
                            "subnet": "24"
                        }
                    ],
                    "lineprotocol": "up ",
                    "macaddress": null,
                    "mediatype": null,
                    "mtu": 1514,
                    "operstatus": "up",
                    "type": null
                },
                "Loopback9": {
                    "bandwidth": 8000000,
                    "description": "__TEST__ 9",
                    "duplex": null,
                    "ipv4": [
                        {
                            "address": "192.168.109.100",
                            "subnet": "24"
                        }
                    ],
                    "lineprotocol": "up ",
                    "macaddress": null,
                    "mediatype": null,
                    "mtu": 1514,
                    "operstatus": "up",
                    "type": null
                }
            },
            "ansible_net_memfree_mb": 2059430,
            "ansible_net_memtotal_mb": 2396128,
            "ansible_net_model": "CSR1000V",
            "ansible_net_serialnum": "9JGOSIUGQVN",
            "ansible_net_version": "16.08.01"
        },
        "changed": false,
        "failed": false
    }
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_hostname": "csr1000v"
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_version": "16.08.01"
}

TASK [debug] ***************************************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "facts_output.ansible_facts.ansible_net_model": "CSR1000V"
}

TASK [Display debug module msg with all variables of interest] *************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "msg": "Device with hostname csr1000v is of model type CSR1000V running software version 16.08.01"
}

PLAY RECAP *****************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=6    changed=0    unreachable=0    failed=0

root@07163e92ec9b:/ansible_local/Decomposing_DataStructures#

```