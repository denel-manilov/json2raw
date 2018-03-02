from sys import argv, exit, stderr
import json


def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)
    exit(1)
    pass


def parse(data, template, prefix=''):
    if type(data) == dict:
        data = data.items()
    elif type(data) == list:
        data = enumerate(data)
    else:
        return data
        pass
    for name, value in data:
        name = (str(prefix) + '_' + str(name)).strip('_')
        if type(value) == dict or type(value) == list:
            parse(value, template=template, prefix=name)
        else:
            try:
                print(template.format(**{"name": name, "value": value}))
            except Exception as e:
                eprint('Format Exception:\n', e, '\nAvailable keys: name, value')
                pass
            pass
        pass
    pass


def main():
    template = '{name}={value}'
    if not argv[1:]:
        eprint('Usage:\n json2raw [-f string] file0.json file1.json')
        pass
    files = argv[1:]
    if argv[1] == '-f':
        if not argv[2:]:
            eprint('-f string\n Format output', 'default:', template)
        template = argv[2]
        files = argv[3:]
        pass
    if not files:
        eprint('Set files')
        pass
    for file in files:
        try:
            content = open(file)
        except FileNotFoundError as e:
            eprint('Cannot load file:', file, "\n", e)
        except Exception as e:
            eprint(e)
            pass
        try:
            data = json.load(content)
        except json.decoder.JSONDecodeError as e:
            eprint('Cannot parse file:', file, "\n", e)
        except Exception as e:
            eprint(e)
            pass
        parse(data=data, template=template)
    pass


if __name__ == '__main__':
    main()
    pass
