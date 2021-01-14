#!/usr/bin/env python

import yaml
import subproces

def getHash():
    return subproces.check_output(['git', 'rev-parse', '--short', 'HEAD'])

with open("kube/blogKube.yaml", 'r') as stream:
    try:
        loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Modify the fields from the dict
loaded['spec']['template']['spec']['containers']['name']['image'] = "Max"

# Save it again
with open("kube/blogKube.yaml", 'w') as stream:
    try:
        yaml.dump(loaded, stream, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)