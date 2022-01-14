import argparse
import requests

parser = argparse.ArgumentParser('Process HTTP')


parser.add_argument('-l', '--url', type=str, help= 'enter url')

args, unknown = parser.parse_known_args()


URL = args.url
r = requests.get(URL)

print(f"From a server <Response [{r.status_code}]>")
print(f"\nList of ignored parameters: {unknown}")