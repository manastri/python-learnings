#!/usr/bin/python3
import socket

# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:

    # Read each line (FQDN) from the input file
    for line in input_file:

        # Strip whitespace and newline characters from the line=False
        fqdn = line.strip()

        try:
            # Look up the A record for the FQDN
            ip_address = socket.gethostbyname(fqdn)

            # Write the FQDN and its A record to the output file
            output_file.write(fqdn + ',' + ip_address + '\n')

        except socket.gaierror as e:
            # If the FQDN cannot be resolved, write an error message to the output file
            output_file.write(fqdn + ',' + str(e) + '\n')
