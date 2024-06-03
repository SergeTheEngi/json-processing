import json

def json_recurse(jsonData):
    for item in jsonData:
        if type(jsonData[item]) == str:
            try:
                jsonData[item] = json.loads(jsonData[item])
                json_recurse(jsonData[item])
            except:pass
        elif type(jsonData[item]) == dict:
            json_recurse(jsonData[item])
        elif type(jsonData[item]) == list:
            for listItem in jsonData[item]:
                json_recurse(listItem)
        else:pass


def json_flatten(y):
    out = {}
    
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a],name + a + '_')
        elif type(x) is list:
            i=0
            for a in x:
                flatten(a,name+str(i)+'_')
                i += 1
        else:
            out[name[:-1]] = x
    
    flatten(y)
    return out


def key_retrieve(jsonFrom,keyFrom,jsonTo,keyTo):
    if keyFrom in jsonFrom:
        jsonTo[keyTo] = jsonFrom[keyFrom]
        return 0
    else:
        return 1


def key_process(jsonFlat,jsonTo,keyAlias,key):
    i = 0

    while True:
        keyFlat = ''

        for pathpiece in keyAlias[key]:
            if pathpiece == list:
                keyFlat = keyFlat + str(i) + '_'
                i += 1
                continue
            keyFlat = keyFlat + pathpiece + '_'
        
        # Delete the last `_` of the flat key
        keyFlat = keyFlat[:-1]
    
        if i == 0: keyOut = key
        if i > 0: keyOut = key + str(i - 1)
        if key_retrieve(
            jsonFlat,
            keyFlat,
            jsonTo,
            keyOut
        ) == 1 or i == 0:break