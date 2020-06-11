import json
import pprint

f = open("./songs.txt", "r")
library = json.loads(f.read())
f.close()

pprint.pprint(library)

