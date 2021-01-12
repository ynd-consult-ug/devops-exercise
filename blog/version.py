import sys
import yaml

def version(a):
    with open('mysecret.yaml') as f:
        doc = yaml.load(f)

    doc['stringData']['IMAGE_VERSION'] = "localhost:5000/unoterr1/blog_pipe:" +str(a)

    with open('mysecret.yaml', 'w') as f:
        yaml.dump(doc, f)

if __name__ == "__main__":
    a = int(sys.argv[1])
    version(a)
