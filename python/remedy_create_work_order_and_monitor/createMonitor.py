## Provisioning task (for configuration stage) python script to create a work order in Remedy
## then monitor that work order for approval before exiting and allowing provisioning to continue

import requests
import time
import json

import sys
sys.path.append('/usr/lib/python3.6/site-packages/')

##from morpheuscypher import Cypher
##c = Cypher(morpheus=morpheus)

## remove this we fake the morpheus dict in development
import fake
c = fake

## debug mode
debug = False

## configuration
remedyUser = c.get("secret/remedyUser")
remedyPassword = c.get("secret/remedyPassword")

## config
remedyHost = "localhost" ## mock server
remedyPort = "9999"

## get a jwt token for the session
def authenticate(username, password):
    print("INFO: authenticating with remedy server to get JWT")

    url = f'http://{ remedyHost }:{remedyPort}/api/jwt/login'
    form = {
        "username": username,
        "password": password,
        "authString": ""
    }

    ## only text/plain here
    header = {
        "accept": "text/plain"
    }

    r = requests.post(url, headers=header, verify=False, data=form)
    if not r.ok:
        print("ERROR: authenticating, response code %s: %s" % (r.status_code, r.text))
        raise Exception("Error authenticating, response code %s: %s" % (r.status_code, r.text))
    else:
        print("INFO: authenticated with remedy server")
        jwt = r.text
        token = "AR-JWT %s" % jwt
        debugP("token with prefix: %s" % token)
        headers = {
            "accept": "application/json",
            "content-type" : "application/json",
            "authorization": token
        }
    return headers

## create the work item
def createWorkOrder(headers):
    print("INFO: creating work order item on remedy server")

    url = f'http://{ remedyHost }:{remedyPort}/api/arsys/v1/entry/SRM:RequestInterface_Create?fields=values(Request%20Number)'

    values = {
        "TitleInstanceID": "<%=instance.name%>",
        "Source Keyword": "Morpheus CMP",
        "Login ID": "<%=customOptions.vmowner%>", ## use email address? instance.createdByEmail
        "OfferingTitle": "Morpheus Provisioned Catalog Item",

        "SR Type Field 10": "Medium", ## Priority
        "SR Type Field 14": "N/A", ## Justification required on high/vhigh priority
        "SR Type Field 15": "Morpheus Catalog Item",  ## Database required
        "SR Type Field 17": "N/A", ## database description
        "SR Type Field 19": "<%=instance.instanceContext%>", ## Server Environment
        "SR Type Field 20": "N/A", ## Function Description
        "SR Type Field 21": "<%=instance.hostname%>", ## Server Name
        "SR Type Field 22": "<%=instance.instanceTypeName%>", ## Server Application
        "SR Type Field 23": "<%=instance.description%>", ## Server application desscription
        "SR Type Field 28": "<%=instance.plan%>", ## Computing reources plan
        "SR Type Field 29": "<%=customOptions.department%>", ## Department Name
        "SR Type Field 30": "<%=instance.backup.enabled%>", ## Backup enabled
        "SR Type Field 31": "Morpheus Instance Type", ## OS type
        "SR Type Field 32": "<%=instance.instanceTypeName%>", ## OS Version
        "SR Type Field 33": "Morpheus Managed", ## Network
        "z1D Action": "CREATE"
    }

    reqBody = {
        "values" : values
    }

    requestNumber = ""
    postData = json.dumps(reqBody)

    debugP(postData)

    r = requests.post(url, headers=headers, verify=False, data=postData)
    if not r.ok:
        print("ERROR: creating request, response code %s: %s" % (r.status_code, r.text))
        raise Exception("Error creating request, response code %s: %s" % (r.status_code, r.text))
    else:
        if r.status_code == 201:
            res = json.loads(r.text)
            requestNumber = res["values"]["Request Number"]
            print("INFO: request created: '%s'" %requestNumber)
    return requestNumber

## poll the work order every minute to check approval status
## looks like status can cycle through many stages Pending, Waiting Approval, Planning, Approved
def monitorWorkOrder(headers, requestNumber):
    print("INFO: monitoring requestNumber '%s' on remedy server" % requestNumber)

    url = f'http://{ remedyHost }:{remedyPort}/api/arsys/v1/entry/SRM:RequestApDetailSignature?fields=values(Request%20Number,Approval%20Status,Approvers)&q=\'Request Number\'="{ requestNumber }"'

    if requestNumber == "":
        print("ERROR: no request number")
        raise Exception("Error no request number")

    approved = False
    startMonitor = time.time()
    while not approved:
        time.sleep(10)
        print("INFO: checking requestNumber '%s' status" % requestNumber)

        ## make call to remedy to check on status of work order
        r = requests.get(url, headers=headers, verify=False, data=None)
        if not r.ok:
            print("ERROR: accessing request, response code %s: %s" % (r.status_code, r.text))
            print("WARN: continuing to poll despite error")
        else:
            if r.status_code == 200:
                res = json.loads(r.text)
                approvalStatus = res["entities"][0]["values"]["Approval Status"]
                if approvalStatus == "Approved":
                    approved = True
            else:
                print("WARN: unexpected response status code %s: %s" % (r.status_code, r.text))

        if approved:
            print("INFO: requestNumber '%s' is approved, continuing" % requestNumber)
        else:
            print("INFO: requestNumber '%s' is not yet approved" % requestNumber)
            elapsedMonitor = time.time() - startMonitor
            log = time.strftime("%Hh %Mm %Ss", time.gmtime(elapsedMonitor))
            if elapsedMonitor > 3600:
                print("WARN: polling approval for requestNumber id '%s' for %s" % (requestNumber, log))

## finish the session
def logout(headers):
    url = f'http://{ remedyHost }:{remedyPort}/api/jwt/logout'

    r = requests.post(url, headers=headers, verify=False, data=None)
    if not r.ok:
        print("WARN: problem logging out of remedy server, response code %s: %s" % (r.status_code, r.text))
    else:
        print("INFO: logged out of remedy server")

## additional debug logging
def debugP(message):
    if debug:
        print("DEBUG:", message)

def main():
    ## retrieve token just form values
    headers = authenticate(remedyUser, remedyPassword)

    ## create the work order
    requestNumber = createWorkOrder(headers)

    ## poll to get approved status
    monitorWorkOrder(headers, requestNumber)

    ## logout and exit
    logout(headers)

## start main execution
main()