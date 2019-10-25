import argparse
import os
import subprocess
import boto3

from utils import safe_create_file

parser = argparse.ArgumentParser(
    description="A script to generate a keypair for aws ec2"
)
parser.add_argument(
    "keypair_name",
    help="Name of the keypair to create. If a keypair already exists with this name, it will be overwritten with a new one.",
)
args = parser.parse_args()

HOME = os.path.expanduser("~")
KEYPAIR_DIR = os.path.join(HOME, ".keypairs")
KEYPAIR_PATH = os.path.join(KEYPAIR_DIR, f"{args.keypair_name}.pem")
LOG_END = "\n\n"

ec2 = boto3.resource("ec2")

# call the boto ec2 function to create a key pair
keypair = ec2.create_key_pair(KeyName=args.keypair_name)
keypair_out = str(keypair.key_material)
print(f"KEYPAIR {args.keypair_name}:")
print(keypair_out, end=LOG_END)

# create a file to store the key locally
outfile = open(safe_create_file(KEYPAIR_PATH), "w")
print(f"Created new keypair pem at {KEYPAIR_PATH}", end=LOG_END)

# capture the key and store it in a file
print(keypair_out, file=outfile)
outfile.close()

# run the permissions
command = f"chmod 400 {KEYPAIR_PATH}"
subprocess.call(command, shell=True)

print("Your keypair is now accessible and ready to use!")
