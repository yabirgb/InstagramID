import json
import urllib2

import sys

name = sys.argv[1]

def extract(name=name):
    #get the .json with the search results
    f = urllib2.urlopen('https://api.instagram.com/v1/users/search?q=' + name +'&client_id=%20c341c2133cea49f3a4e38e21d35cda88')
    #load the .json
    resultados = json.load(f)

    #uncomment to save the .json of the search
    # file_ = open(str(name) + '.json', 'w')
    # file_.write(str (resultados))
    # file_.close()

    return resultados["data"][0]["id"]

if __name__ == "__main__":
    print("Id of " + name + ' is ' + extract())
