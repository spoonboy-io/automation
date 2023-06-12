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
        if !hasCacheVersion:
            print("something to the above effect")
        else:
            ## can we look up the equivalent virtual image in morpheus?
            ## we will have name, version, and we can look for later ID version for extra valids
            ## if we can find it, and be certain, update the node type with new virtual image data


if writeCache:
    ## write or update cache
    f = open(cacheFile, "w")
    f.write(json.dumps(nodeTypes))
    f.close()

