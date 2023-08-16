#!/usr/bin/env python3

import subprocess
import sys
from datetime import datetime, date

args = sys.argv

status = ""

if len(sys.argv) == 1:
    print("Error - No Domain Name List was found...")
    status = "break"

elif len(sys.argv) > 2:
    print("Error - Invalid Arguments given. Please check again...")
    status = "break"

try:
    if status != "break":

        dns_text_file = args[1]
        print("+---------------------------------------------------------------------------------------+")
        print("| " + ("Domain Name").ljust(30) + " |\t" + "Pointed IP Address" + "\t|" + "\tName Serverss\t|")

        with open(dns_text_file, 'r') as file:
            for dns_name in file:
                
                command = f"dig {dns_name.strip()} @8.8.8.8"

                output = subprocess.check_output(command, shell=True, universal_newlines=True)
                lines = output.split("\n")
                if ";; ANSWER SECTION:" in output:
                    
                    answer_section_index = lines.index(";; ANSWER SECTION:")
                    next_line_index = answer_section_index + 1

                    dns_results = lines[next_line_index].strip()
                    splitted_dns_results = dns_results.strip().split()
                    print("+---------------------------------------------------------------------------------------+")
                    print("| " + splitted_dns_results[0].ljust(30) + " |\t" + splitted_dns_results[-1] + "\t\t|")
                else:
                    print("+---------------------------------------------------------------------------------------+")
                    print("| " + dns_name.strip().ljust(30) + " |\tUnable to resolve" + "\t|")

        print("+---------------------------------------------------------------------------------------+")
        print("| Scanned Results on " + str(date.today()) + " at " + str(datetime.now().time().strftime("%H:%M:%S")) + "\t\t\t|")
        print("+---------------------------------------------------------------------------------------+")

except FileNotFoundError:
    print("Error - File not found")