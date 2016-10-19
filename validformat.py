import sys
import argparse
import json
import xml 
import yaml 

def validjson(s):
    try:
        json.load(s)
        print("Valid.")
    except:
        raise ValueError("Invalid Json.")


def validyaml(s):
    try:
        yaml.load(s)
        print("Valid.")
    except:
        raise ValueError("Invalid Json.")


def validxml(s):
    try:
        xml.etree.ElementTree.parse_string(s)
        print("Valid")
    except:
        raise ValueError("Invalid Xml.")


def cli():
    parser = argparse.ArgumentParser(description="Validate file format")
    parser.add_argument('--json', action="store_true", help="validate json.", dest='json')
    parser.add_argument('--yaml', action="store_true", help="validate yaml.", dest='yaml')
    parser.add_argument('--xml', action="store_true",help="validate xml.", dest='xml')
    
    args = parser.parse_args()

    if args.json:
        validjson(sys.stdin)
    elif args.yaml:
        validyaml(sys.stdin)
    elif args.xml:
        validxml(sys.stdin)
    else:
        raise ("Unknown argument")

if __name__ == "__main__":
    cli()