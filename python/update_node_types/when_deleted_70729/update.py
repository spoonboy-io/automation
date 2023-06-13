import requests
from os.path import exists
import json

## remove this we fake the morpheus dict in development
import fake
morpheus = fake.morpheus

## config
host = morpheus["morpheus"]["applianceHost"]
token = "Bearer %s" %(morpheus["morpheus"]["apiAccessToken"])
headers = {
    "accept": "application/json",
    "authorization": token
}

cacheFile = "azureNodeTypeCache.json" ## dev
##cacheFile = "/tmp/azureNodeTypeCache.json" ## morpheus
hasCacheVersion = False
cacheNodeTypes = []

getImages = "https://%s/api/virtual-images?max=1000&filterType=Synced&imageType=vhd" % (host)
getNodeTypes = "https://%s/api/library/container-types?max=2000&provisionType=azure&sort=id&direction=asc" % (host)

## check if cached data exists and if true load it
if exists(cacheFile):
    hasCacheVersion = True
    f = open(cacheFile, "r")
    cache = f.read()
    cacheNodeTypes = json.loads(cache)
    print("cached node types have been read from disk")

## get the virtual image and node data
res = requests.get(getImages, headers=headers, verify=False)
virtualImages = res.json()["virtualImages"]

res = requests.get(getNodeTypes, headers=headers, verify=False)
nodeTypes = res.json()["containerTypes"]

## iterate nodes for nodes with null virtual image
## nocache, if we get nulls we won't cache the
writeCache = True
for nt in nodeTypes:
    if nt["virtualImage"] is None:
        ## we have orphans, we don't want to cache the response
        writeCache = False

        ## if no cache exists and we have nulls there's nothing to do, but log that the nulls have been found
        ## and that the node types will have to be manually updated
        if hasCacheVersion:
            ## lookup the node in the cached data
            for nc in cacheNodeTypes:
                if nc["id"] == nt["id"]:
                    ## get the virtual image that was attached
                    vi = nt["virtualImage"]
                    if vi is not None:
                        ## get then update the node type with virtual image
                        apiNodeType = "https://%s/api/library/container-types/%s" % (host, nt["id"])
                        res = requests.get(apiNodeType, headers=headers, verify=False)
                        nodeType = res.json()

                        ## update the info
                        nodeType["containerType"]["virtualImage"]["id"] = vi["id"]
                        nodeType["containerType"]["virtualImage"]["name"] = vi["name"]

                        putData = json.dumps(nodeType)

                        ## make the put request with data
                        res = requests.put(apiNodeType, data=putData, headers=headers, verify=False)
                        msg = ""
                        if res.status_code == 200:
                            msg = "Response: %s, Node type: %s (id: %s) was relinked to virtual image; %s (id: %s)" % (res.status_code, nt["name"], nt["id"], vi["name"], vi["id"])
                        else:
                            msg = "ErrResponse: %s, Node type: %s (id: %s) virtual image will need to be added manually" % (res.status_code, nt["name"], nt["id"])
                        print(msg)
        else:
            ## nothing to be done output some information about the node type
            msg = "Node type: %s (id: %s) is disconnected from a virtual image, there is no cache so a virtual image will need to be added manually" % (nt["name"], nt["id"])
            print(msg)

## write or update cache conditionally
if writeCache:
    f = open(cacheFile, "w")
    f.write(json.dumps(nodeTypes))
    f.close()
    msg = "node types cached for tracking in file: %s" % cacheFile
    print(msg)