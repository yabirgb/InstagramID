#Needed imports
import json
import urllib.request
import sys

#the user we want the info
name = sys.argv[1]


def extract(name=name):
    #generate the url
    url = 'https://api.instagram.com/v1/users/search?q=' + name +'&client_id=%20c341c2133cea49f3a4e38e21d35cda88'

    #open the url, read it and decode to UTF-8
    f = urllib.request.urlopen(url)
    data = f.read()
    results = json.loads(data.decode('utf8'))


    #Uncomment this if you want to save the file of the search as a .json
    # file_ = open(str(name) + '.json', 'w')
    # file_.write(str (resultados))
    # file_.close()

    #return the number from the json
    return results["data"][0]["id"]

if __name__ == "__main__":
    print("The Id of " + name + ' is ' + extract())
