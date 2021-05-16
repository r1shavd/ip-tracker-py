"""
IP Tracker

This is a tool which serves the feature of fetching out information about any IP address (i.e., any computer device that is publically connected to the internet, and we just need the address of it). The tool is written in Python3.
Dependencies :
1. requests - python3 module

Usage :
1. First clone the repository from github mirror of it, using the command 'git clone https://github.com/anirudhataliyan/IPTracker/' [Type these commands in the terminal].
2. Use this command to install the dependencies - 'pip3 install requests'.
3. Run the script using these commands - 'python3 IPTracker.py'

Author : Rishav Das (https://github.com/rdofficial/)
Created on : May 9, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 15, 2021

Changes made in last modification:
1. Replaced the older way of cleaning console screen with the newer way, which apparently works with both linux as well as windows. The previous version was only working for linux (or operating systems which supported unix commands).

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the requird functions and modules
try:
    from os import system
    from sys import platform
    from json import loads
    from urllib import request
except Exception as e:
    # If there are any errors encountered during the importing of the modules, then we display the error on the console screen

    input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
    exit()

# Defining the ANSII color codes for colored output
if 'linux' in platform:
    # If the current operating system is linux, then we continue to define the color codes

    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    red_rev = '\033[07;91m'
    yellow_rev = '\033[07;92m'
    defcol = '\033[00m'
    clear = 'clear'
else:
    red = ''
    green = ''
    yellow = ''
    blue = ''
    red_rev = ''
    yellow_rev = ''
    defcol = ''
    clear = 'cls'

def main():
    # Displaying the banner and other info
    system(clear)
    print(f'\t\t[ {yellow_rev}IP Tracker{defcol} ]\n')  # The tool name
    print(f'[{green}!{defcol}]-------------{yellow}About author{defcol}-------------[{green}!{defcol}]\n[{red}#{defcol}] Instagram : {yellow}@rishavd._{defcol}\n[{red}#{defcol}] Github : {yellow}https://github.com/rdofficial/{defcol}\n')  # The author's information
    print(f'[{green}!{defcol}]-----------------{yellow}Note{defcol}-----------------[{green}!{defcol}]\n[{red}1{defcol}] Make sure you are connected to internet.\n[{red}2{defcol}] Make sure the IP address you are looking is a public IP.\n[{red}3{defcol}] If you want to stop the script in the middle, then press CTRL+C key combo.\n')

    # Asking the user to enter the IP Address
    ipAddress = input('Enter the IP address : ')

    # Checking if the user entered blank value or not
    if len(ipAddress) == 0:
        # If the user entered value is blank, then we display the error on the console screen

        input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
        return 0
    else:
        # If the user entered value is not blank, then we continue

        # Sending a GET HTTP request
        response = request.urlopen(f'http://ipinfo.io/{ipAddress}')
        if response.status == 200:
            # If the response we recieved indicates successfull HTTP request

            response = response.read().decode()  # Reading the response from the server
            response = loads(response)  # Parsing the response in JSON format
            for item in response:
                print(f'[{green}#{defcol}] %-25s    :    {yellow}%-25s{defcol}' %(item.upper(), response[item]))
        else:
            # If the response we recieved indicates failed HTTP request, then we display the error on the console screen

            input(f'{red_rev}[ Error : Failed to fetch the information about the specified IP address ]{defcol}\nPress enter key to continue...')
            return 0

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit

        exit()
    except Exception as e:
        # If we encounter any error during the process, then we display the error on the console screen

        input(f'{red_rev}[ Error : {e} ]{defcol}\nPress enter key to continue...')
        exit()
