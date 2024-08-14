import base64
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Decode Base64 data and save to a file.')
parser.add_argument('base64_data', type=str, help='Base64 encoded data')
parser.add_argument('output_file', type=str, help='File to save the decoded data')

# Parse arguments
args = parser.parse_args()

# Decode the Base64 data
decoded_bytes = base64.b64decode(args.base64_data)

# Save the decoded data to the specified file
with open(args.output_file, 'wb') as file:
    file.write(decoded_bytes)

print(f'Decoded data saved to {args.output_file}')
