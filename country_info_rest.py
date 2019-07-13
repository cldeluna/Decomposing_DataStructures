#!/usr/bin/python -tt
# Project: scripts
# Filename: country_info_rest
# claud
# PyCharm


__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "7/7/2019"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import argparse
import requests
import json
import os

def one_level_down(data, depth):
    
    lev = "levels"

    if depth == 1:
        lev == "level"

    data_typ = type(data)

    if data_typ == int or data_typ == float:
        data_len = len(str(data))
    else:
        data_len = len(data)

    print(f"\tThe data structure {depth} {lev} deep is a {data_typ}")
    print(f"\tThe length of the data structure {depth} {lev} deep is {data_len}")

    return data_typ, data_len


def decompose(results):

    print(f"\n==== EXECUTING DECOMPOSE FUNCTION ====\n")

    print(f"\nOuter structure (0) levels deep:")
    one_level_down(results, 0)

    index = 1
    print(f"\nOne level deep:")
    for line in results:

        data_type, data_length = one_level_down(line, index)

        if data_type == dict:
            print(f"\n\tDictionary keys are {line.keys()}\n")

            for key, value in line.items():
                print(f"\t\tKey: {key} \tValue: {value}\n")
        elif data_type == list:
            print(f"List elements are: \n\t{line}")

    print(f"\n\t===== Plucking out specific data:\n")
    print(f'\t2 Letter Country Code: \t\t\t\t{results[0]["alpha2Code"]}')
    print(f'\tFirst (0 index) International Calling Code: \t{results[0]["callingCodes"][0]}')
    print(f'\tList of International Calling Code: \t\t{results[0]["callingCodes"]}')
    print(f"\t==========================================\n")


def rest_get_country_by_name(name):
    """
    Function to queary the REST Countries REST API for information about a country
    """

    url = f"https://restcountries.eu/rest/v2/name/{name}"

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "3dfa7645-10bc-4730-1361-e631ee8e80f4"
    }

    return requests.request("GET", url, headers=headers)


def main():
    """
    Base code from Postman code generator
    """

    # Get the Current working directory so it can be displayed later when the output file is saved
    cwd = os.getcwd()

    response = rest_get_country_by_name(arguments.cname)

    # Pring the actual REST response which will show the returning HTML Code
    print(f"\nPrinting the response object will display the HTML return code: {response}\n")

    print(f"Look at the options for the response object:\n{dir(response)}\n")

    print(f"Printing the response text as is: {response.text}\n")

    # Load the response text into a JSON object for easier manipulation (printing and saving to a formatted file)
    resp_text_as_json_object = json.loads(response.text)

    print(f"\nPrinting the response text with JSON formatting:\n{json.dumps(resp_text_as_json_object, indent=4)}\n")

    output_fn = f"{arguments.cname}_country_info.json"

    with open(output_fn, "w") as text_file:
        text_file.write(json.dumps(resp_text_as_json_object,indent=4))

    print(f"REST response output saved to file {output_fn} in the following directory:\n{cwd}")

    # Send the JSON object. If you send the response.text its a string.
    if arguments.decompose:
        decompose(resp_text_as_json_object)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Call REST Countries REST API with a country name.",
                                     epilog="Usage: 'python country_info_rest.py' without the --cname argument the script will use the default country name of Mexico. Usage with optional name parameter:  'python country_info_rest.py -n Singapore'. Note: this is a python3 script.")

    #parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-n', '--cname', help='Country Name to override default (Mexico)', default="Mexico")

    parser.add_argument('-d', '--decompose', help='Execute a function to help decompose the response', action='store_true')

    arguments = parser.parse_args()
    main()


