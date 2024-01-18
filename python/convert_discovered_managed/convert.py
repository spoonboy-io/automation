## python script to conver discovered vm(s) to managed

import requests
import urllib3
import time
import json

import sys
sys.path.append('/usr/lib/python3.6/site-packages/')

## remove this we fake the morpheus dict in development
import fake
morpheus = fake.morpheus

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## config
host = morpheus["morpheus"]["applianceHost"]
token = "Bearer %s" %(morpheus["morpheus"]["apiAccessToken"])
headers = {
    "accept": "application/json",
    "authorization": token
}

## debug mode, when on, nothing runs against the morpheus api, but we can see the actions
## the script would will take when debug off, plus additional logging
debug = True

## we will have an array of VM names once we parse what could be a single or comma-delimited
## list of vm names from the custom option input field
inputList = morpheus["customOptions"]["vmList"]

## parses the input in the custom option
def parseCustomOption():
    debugP("parsing the custom option input to extract VM names: " + inputList)

    ## check not empty
    if list == "":
        print("WARN: no data supplied in custom option")
        return

    vmList = inputList.split(",")

    for i in range (len(vmList)):
        ## trim spaces
        vmList[i] = vmList[i].strip()

    print("INFO: parsed the data from the custom option")
    debugP(vmList)
    return vmList

## we check all VMs listed exist as discovered
## we fail if there are errors rather than proceed and perform a partial transaction
def checkExistDiscovered(vmList):
    goodList = True
    vmDict = {}
    debugP("checking vms exist as discovered")

    ## get discovered
    url = f'https://{ host }/api/servers?managed=false&max=10000'
    r = requests.get(url, headers=headers, verify=False)

    if not r.ok:
        print("ERROR: getting discovered vms : Response code %s: %s" % (r.status_code, r.text))
        raise Exception("Error getting discovered vms: Response code %s: %s" % (r.status_code, r.text))
    else:
        print("INFO: got discovered vms")

    data = r.json()

    ## check we have data
    cnt = len(data['servers'])
    if cnt == 0:
        print("WARN: no discovered servers found")
        goodList = False
        return

    debugP("discovered virtual machines: %s" % cnt)
    ## checking each exists
    for vm in vmList:
        found = False
        for discovered in data["servers"]:
            if vm == discovered["name"]:
                found = True
                ## we are capturing the id with the name in a dict for the request
                vmDict[vm] = discovered["id"]
                print("INFO: '%s' was found as discovered, id: %s" % (vm, discovered["id"]))

        if not found:
            print("WARN: '%s' was not found as discovered" % vm)
            goodList = False

    return goodList, vmDict

def convertToManaged(vmDict):
    print("INFO: converting VMs to managed")

    for vm in vmDict:
        debugP("converting vm: %s (id:%s)" %(vm, vmDict[vm]))
        id = vmDict[vm]
        url = f'https://{ host }/api/servers/{ id }/make-managed'
        jbody = {"installAgent": False}
        body = json.dumps(jbody)
        debugP("debug mode is on. no update will be made")
        if not debug:
            print("INFO: sending request to convert VM %s to managed" % vm)
            r = requests.put(url, headers=headers, verify=False, data=body)
            data = r.json()
            if not r.ok:
                print("ERROR: converting to managed: Response code %s: %s" % (r.status_code, r.text))
                raise Exception("Error converting to managed: Response code %s: %s" % (r.status_code, r.text))
            else:
                print("INFO: VM '%s' successfully converted to managed" % vm)

        ## pause so we don't hammer the appliance
        time.sleep(1)

## additional debug logging
def debugP(message):
    if debug:
        print("DEBUG:", message)

## main execution path
def main():
    ## the vm or vms from teh custom option / input
    vmList = parseCustomOption()

    ## check the vms all exist as discovered
    ok, vmDict = checkExistDiscovered(vmList)
    debugP("dict of vms names with their id")
    debugP(vmDict)
    if not ok:
        print("ERROR: not proceeding, not all VMs requested could be found or exist as discovered")
        raise Exception("ERROR: not proceeding, not all VMs requested could be found or exist as discovered")

    ## if good, proceeding to make convert to managed
    convertToManaged(vmDict)

## call entry point
main()