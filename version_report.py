#! /usr/bin/env python

import csv
import os
import argparse
from datetime import datetime
from os.path import expanduser
from sys import exit
from sys import argv
from tabulate import tabulate
from genie.conf import Genie

############# USER DEFINED VARIABLES #############
directory = expanduser("~")
file_name = 'version_report'
headers = ['Device Name', 'OS', 'Model', 'Image', 'Serial Number']


def get_details():
    # Load the testbed of devices and credentials
    testbed = Genie.init('testbed.yml')
    global results

    # Using Genie to gather the data from the devices and store in a list of lists.
    for name in testbed.devices:
        testbed.devices[name].connect()
        version = testbed.devices[name].parse("show version")
        # If is NXOS as uses completely different data structure
        if 'platform' in version.keys():
            dev_table = [name, version['platform']['os'], version['platform']['hardware']['chassis'],
                        version['platform']['software']['system_version'], version['platform']['hardware']['processor_board_id']]
        # If is IOSXE as chassis different in IOSXE and IOS data structures
        elif version['version']['os'] == 'IOS-XE':
            dev_table = [name, version['version']['os'], version['version']['chassis'],
                        version['version']['version_short'], version['version']['chassis_sn']]
        # IF IOSv
        elif version['version']['os'] == 'IOSv':
            dev_table = [name, version['version']['os'], version['version']['platform'],
                        version['version']['version_short'], version['version']['chassis_sn']]
        # Creates a list of lists of all devices
        results.append(dev_table)
        testbed.devices[name].disconnect()

# Prints a table of the devices output to screen
def create_table():
    print(tabulate(results, headers, tablefmt="fancy_grid"))

# Creates a CSV of the devices output
def create_csv():
    file_name_date = args['filename'] + '_' + str(datetime.now().strftime('%Y-%m-%d_%H%M')) + ".csv"
    filename = os.path.join(args['location'], file_name_date)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for x in results:
            writer.writerow(x)
    print('File {} has been created'.format(filename))


# Optional flags user can enter to customise what is run, if nothing is entered uses the default options
parser = argparse.ArgumentParser()
parser.add_argument('output', default='both', nargs='?', choices=['csv', 'table', 'both'], help='Display a Table or Save as a CSV (default: %(default)s)')
parser.add_argument('-f', '--filename', default=file_name, help='Name of the CSV (default: %(default)s)')
parser.add_argument('-l', '--location', default=directory, help='Location to save the CSV (default: %(default)s)')
args = vars(parser.parse_args())

# Checks that the entered location exists.
if args['location'] != directory:
    if not os.path.exists(args['location']):
        print('!!! Error with the location {}. Double check and rerun or leave blank to use the default of home directory!!!'.format(args['location']))
        exit(0)

# Runs the functions based on options entered
results = []
get_details()
if args['output'] == 'table':
    create_table()
elif args['output'] == 'csv':
    create_csv()
elif args['output'] == 'both':
    create_table()
    create_csv()
