from time import sleep
import requests

url_string = 'https://webapp4.asu.edu/catalog/myclasslistresults?t=2227&s={}&n={}&hon=F&promod=F&e=open&page=1'

classes = [
     ['CSE','468'],
     ['ENT','340'],
     ['CSE','355'],
]

def main():
     while True:
          for c in classes:
               t = requests.get(url_string.format(c[0],c[1]))
               if t.text.__contains__('informal'):
                    print('class found for {} {}'.format(c[0],c[1]))

if __name__ == '__main__':
     main();

