import requests
from os.path import exists
import json
import urllib3

## disable insecure warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## remove this we fake the morpheus dict in development
import fake
morpheus = fake.morpheus

## additional logging
def debugP(message):
    if debugMode:
        print(message)

## test mode (will not update Morpheus, but will output the payloads that would be sent
testMode = True

## debug mode will provide additional logging when set to True
debugMode = True

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
updatesMade = False
cacheNodeTypes = []

## there are some system node types which are not associated with a virtual image
## whether this is also an effect of the Azure sync issue I don't kmow but can't know what to link them to
## this script requires we build a cache, and for that we need no unlinked node types, at least once
## so this array allows us to maintain a list of node types (by id) which we can ignore if they are null
excludeNodeTypeList = [5, 333]

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
debugP("%s synced virtual images found" % len(virtualImages))

res = requests.get(getNodeTypes, headers=headers, verify=False)
nodeTypes = res.json()["containerTypes"]
debugP("%s node types found" % len(nodeTypes))

## iterate nodes for nodes with null virtual image
## nocache, if we get nulls we won't cache the
writeCache = True

## inform of status
if testMode:
    print("Script is executing in test mode, no updates will be made")

if debugMode:
    print("Script is executing in debug mode, output will be verbose")

print("Checking node types")
for nt in nodeTypes:
    debugP("Checking node type %s (id: %s)" % (nt["name"], nt["id"]))
    if nt["id"] not in excludeNodeTypeList:
        if nt["virtualImage"] is None:
            ## we have orphans, we don't want to cache the response
            writeCache = False

            ## if no cache exists and we have nulls there's nothing to do, but log that the nulls have been found
            ## and that the node types will have to be manually updated
            if hasCacheVersion:
                ## lookup the node in the cached data
                for nc in cacheNodeTypes:
                    if nc["id"] == nt["id"]:
                        msg = "Found cached version of '%s' node type with missing image" % nc["name"]
                        print(msg)

                        ## get the virtual image that was attached
                        vi = nc["virtualImage"]
                        if vi is not None:
                            ## get then update the node type with virtual image
                            apiNodeType = "https://%s/api/library/container-types/%s" % (host, nt["id"])
                            res = requests.get(apiNodeType, headers=headers, verify=False)
                            nodeType = res.json()

                            ## update the info
                            newImageFound = False
                            for virtualImage in virtualImages:
                                if vi["name"] == virtualImage["name"]:
                                    updatedVirtualImage = {
                                        "id": virtualImage["id"],
                                        "name": virtualImage["name"]
                                    }

                                    nodeType["containerType"]["virtualImage"] = updatedVirtualImage

                                    putData = json.dumps(nodeType)

                                    ## make the put request with data (if not dev)
                                    if not testMode:
                                        res = requests.put(apiNodeType, data=putData, headers=headers, verify=False)
                                        msg = ""
                                        if res.status_code == 200:
                                            msg = "Response: %s, Node type: %s (id: %s) was relinked to virtual image; %s (id: %s)" % (res.status_code, nt["name"], nt["id"], vi["name"], vi["id"])
                                        else:
                                            msg = "ErrResponse: %s, Node type: %s (id: %s) virtual image will need to be added manually" % (res.status_code, nt["name"], nt["id"])
                                            print(msg)
                                    else:
                                        print("Test mode: payload to update node with new virtual image:")
                                        print(nodeType)

                                    newImageFound = True
                                    updatesMade = True

                            if not newImageFound:
                                msg = "Could not identify new image for '%s' based on virtual image name, it remains null in node type" % nt["name"]
            else:
                ## nothing to be done output some information about the node type
                msg = "Node type: %s (id: %s) is disconnected from a virtual image, there is no cache so a virtual image will need to be added manually" % (nt["name"], nt["id"])
                print(msg)
        else:
            msg = "Node type: %s (id: %s) has a virtual image attached, skipping.." % (nt["name"], nt["id"])
            debugP(msg)
    else:
        msg = "Node type %s (id: %s) in excluded list, skipped.." % (nt["name"], nt["id"])
        print(msg)

if not updatesMade:
    print("There where no updates which could be made by the script")

## write or update cache conditionally
if writeCache:
    f = open(cacheFile, "w")
    f.write(json.dumps(nodeTypes))
    f.close()
    msg = "Node types cached for tracking in file: %s" % cacheFile
    print(msg)

print("Script execution completed")