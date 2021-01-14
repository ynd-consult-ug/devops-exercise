import sys
import yaml

def version(a, b, c, d):
    with open('mysecret.yaml') as f:
        doc = yaml.load(f)

#   doc['spec']['spec']['stringData']['IMAGE_VERSION'] = "localhost:5000/unoterr1/blog_pipe:" +str(a)
#    doc['spec']['spec']['containers'][0]['image'] = "localhost:5000/unoterr1/blog_pipe:" +str(a)
    doc['stringData']['DATABASE_HOST'] = a
    doc['stringData']['DATABASE_NAME'] = b
    doc['stringData']['DATABASE_PASSWORD'] = c
    doc['stringData']['DATABASE_USERNAME'] = d

    with open('mysecret.yaml', 'w') as f:
        yaml.dump(doc, f)

if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    c = str(sys.argv[3])
    d = str(sys.argv[4])
    version(a, b, c, d)
