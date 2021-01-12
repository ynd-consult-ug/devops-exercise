import sys
#from ruamel.yaml import YAML

# def version(a):
#     file_name = 'mysecret.yaml'
#     config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
#     ver = config['stringData']
#     ver[0]['IMAGE_VERSION'] = a
#     with open('mysecret.yaml', 'w') as fp:
#         yaml.dump(config, fp)
#     print("Your version is: ", a) 

import yaml

def version(a):
    with open('mysecret.yaml') as f:
        doc = yaml.load(f)

    doc['stringData']['IMAGE_VERSION'] = a

    with open('mysecret.yaml', 'w') as f:
        yaml.dump(doc, f)

# def version(a):
#     yaml = YAML()
#     mf = 'mysecret.yaml'
#     doc = yaml.load(mf)
#     doc[0]['IMAGE_VERSION'] = a
#     yaml.dump(doc, mf)

if __name__ == "__main__":
    a = int(sys.argv[1])
    version(a)

# yaml = ruamel.yaml.YAML()
# yaml.preserve_quotes = True
# with open('input.yaml') as fp:
#     data = yaml.load(fp)
# for elem in data:
#     if elem['name'] == 'IMAGE_VERSION':
#          elem['value'] = 1234
#          break  # no need to iterate further
# yaml.dump(data, sys.stdout)
