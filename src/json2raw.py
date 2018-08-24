#!/usr/bin/env python3

""" json2raw is a simple utility that transforms the JSON structure into a key / value list. """
import json
import sys


def eprint(*args, **kwargs):
    """ Print to stderr """
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)

def parse(data, template, prefix=''):
    """ Parse json """
    if isinstance(data, dict):
        data = data.items()
    elif isinstance(data, list):
        data = enumerate(data)
    else:
        return data
    for name, value in data:
        name = (str(prefix) + '_' + str(name)).strip('_')
        if isinstance(value, (dict, list)):
            parse(value, template=template, prefix=name)
        else:
            try:
                print(template.format(**{"name": name, "value": value}))
            except KeyError as tpl_e:
                eprint('Format Exception:\n', tpl_e, '\nAvailable keys: name, value')
    return None


def main():
    """ Main """
    template = '{name}={value}'
    if not sys.argv[1:]:
        eprint('Usage:\n json2raw [-f string] file0.json file1.json')
    files = sys.argv[1:]
    if sys.argv[1] == '-f':
        if not sys.argv[2:]:
            eprint('-f string\n Format output', 'default:', template)
        template = sys.argv[2]
        files = sys.argv[3:]
    if not files:
        eprint('Set files')
    for file in files:
        try:
            content = open(file)
        except FileNotFoundError as fnf_e:
            eprint('Cannot load file:', file, "\n", fnf_e)
        try:
            data = json.load(content)
        except json.decoder.JSONDecodeError as jd_e:
            eprint('Cannot parse file:', file, "\n", jd_e)
        parse(data=data, template=template)

if __name__ == '__main__':
    main()
