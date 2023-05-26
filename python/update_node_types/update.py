import requests
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

getImages = "https://%s/api/virtual-images?max=1000&filterType=Synced&&imageType=vhd" % (host)
getNodeTypes = "https://%s/api/library/container-types?max=2000&offset=1400&sort=id&direction=asc" % (host)

## get the virtual image and node data
res = requests.get(getImages, headers=headers, verify=False)
virtualImages = res.json()["virtualImages"]

res = requests.get(getNodeTypes, headers=headers, verify=False)
nodeTypes = res.json()["containerTypes"]

imageInfo = []

## iterate the virtual images
for vi in virtualImages:
    ## if subscription we are interested
    if "/subscriptions" in vi["externalId"]:
        ## split the external id
        sp = vi["externalId"].split("/versions/")
        if len(sp) == 2: ## only on refs with versions
            imageData = {}

            ## collect the data we're interested in
            imageData["id"] = vi["id"]
            imageData["name"] = vi["name"]
            imageData["prefix"] = sp[0]
            imageData["version"] = sp[1]
            imageData["createdDate"] = vi["dateCreated"]

            ## store it
            imageInfo.append(imageData)

## now we can work against the data we need
for vi in imageInfo:
    ## we catch the latest latest version info
    latest = {}
    for vi2 in imageInfo:
        ## test for later version
        if vi["prefix"] == vi2["prefix"] and vi2["createdDate"] > vi["createdDate"]:
            ## so now we know that an image has a later version, replace latest
            latest = vi2

    if len(latest) != 0:
        ## we need to find node types which use the old node type and update them
        for nt in nodeTypes:
            if nt["virtualImage"] is not None:
                if nt["virtualImage"]["id"] == vi["id"]:
                    ## if use image get and update node type to use new version
                    apiNodeType = "https://%s/api/library/container-types/%s" % (host, nt["id"])
                    res = requests.get(apiNodeType, headers=headers, verify=False)
                    nodeType = res.json()

                    ## update
                    nodeType["containerType"]["virtualImage"]["id"] = latest["id"]
                    nodeType["containerType"]["virtualImage"]["name"] = latest["name"]
                    nodeType["containerType"]["containerVersion"] = latest["version"]

                    putData = json.dumps(nodeType)

                    ## make the put request with data
                    res = requests.put(apiNodeType, data=putData, headers=headers, verify=False)
                    print(res)