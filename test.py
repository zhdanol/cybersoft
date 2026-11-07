import json

def read_file(config):
    with open(config, 'r', encoding='utf-8') as f:
        return json.load(f)


file = read_file(input())



def parse_port(text):
    try:
        return text
    except ValueError:
        return None

text = parse_port(file)
print(text)