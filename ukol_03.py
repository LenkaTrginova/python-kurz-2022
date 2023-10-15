#Zadání

import json
with open('body.json', encoding='utf-8') as file:
    body = json.load(file)

hodnoceni = {}

for jmeno, body in body.items():
    if body >= 60:
        hodnoceni[jmeno] = "Pass"
    else:
        hodnoceni[jmeno] = "Fail"

with open('prospech.json', 'w') as file:
    json.dump(hodnoceni, file)
