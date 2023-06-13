// Dev/Test data - snapshot of return from the Morpheus API
let data = {
    "clusters": [
        {
            "id": 3,
            "name": "MKS Test",
            "code": null,
            "category": null,
            "visibility": "private",
            "description": null,
            "location": null,
            "enabled": true,
            "serviceUrl": "https://10.32.20.166:6443",
            "serviceHost": null,
            "servicePath": null,
            "serviceHostname": null,
            "servicePort": 22,
            "serviceUsername": null,
            "servicePassword": null,
            "servicePasswordHash": null,
            "serviceToken": "************",
            "serviceTokenHash": "48468407f25fd559877c8793abfb846da4722b14684fdb5bade1f3c25bf57d33",
            "serviceAccess": "************",
            "serviceAccessHash": "c9088ad50c2783b6f6c81e1e46ed8f8f954ddf31cd97740fb70164209213b570",
            "serviceCert": null,
            "serviceCertHash": null,
            "serviceVersion": "v1.26.1",
            "searchDomains": null,
            "enableInternalDns": false,
            "internalId": null,
            "externalId": null,
            "datacenterId": null,
            "status": "ok",
            "statusDate": "2023-06-13T12:01:14Z",
            "statusMessage": "",
            "inventoryLevel": "full",
            "lastSync": "2023-06-13T12:01:14Z",
            "nextRunDate": "2023-06-13T12:06:14Z",
            "lastSyncDuration": 790,
            "dateCreated": "2023-05-12T13:48:05Z",
            "lastUpdated": "2023-06-13T12:01:14Z",
            "managed": true,
            "labels": [],
            "serviceEntry": null,
            "createdBy": {
                "id": 1,
                "username": "admin"
            },
            "userGroup": null,
            "layout": {
                "id": 218,
                "name": "MKS Kubernetes 1.26 Cluster on Ubuntu 20.04",
                "provisionTypeCode": "vmware"
            },
            "owner": {
                "id": 1,
                "name": "Neo"
            },
            "servers": [
                {
                    "id": 14,
                    "name": "MKS 1-worker-1",
                    "typeSet": {
                        "id": 438,
                        "code": "kubernetes-1.26.1-ubuntu-20.04.1-worker-vmware-amd64-set",
                        "name": "kubernetes worker"
                    },
                    "computeServerType": {
                        "id": 108,
                        "code": "vmwareKubeWorker",
                        "nodeType": "kube-worker"
                    }
                },
                {
                    "id": 16,
                    "name": "MKS 1-worker-3",
                    "typeSet": {
                        "id": 438,
                        "code": "kubernetes-1.26.1-ubuntu-20.04.1-worker-vmware-amd64-set",
                        "name": "kubernetes worker"
                    },
                    "computeServerType": {
                        "id": 108,
                        "code": "vmwareKubeWorker",
                        "nodeType": "kube-worker"
                    }
                },
                {
                    "id": 13,
                    "name": "MKS 1-master",
                    "typeSet": {
                        "id": 437,
                        "code": "kubernetes-1.26.1-ubuntu-20.04.1-vmware-amd64-set",
                        "name": "kubernetes master"
                    },
                    "computeServerType": {
                        "id": 107,
                        "code": "vmwareKubeMaster",
                        "nodeType": "kube-master"
                    }
                },
                {
                    "id": 15,
                    "name": "MKS 1-worker-2",
                    "typeSet": {
                        "id": 438,
                        "code": "kubernetes-1.26.1-ubuntu-20.04.1-worker-vmware-amd64-set",
                        "name": "kubernetes worker"
                    },
                    "computeServerType": {
                        "id": 108,
                        "code": "vmwareKubeWorker",
                        "nodeType": "kube-worker"
                    }
                }
            ],
            "accounts": [],
            "integrations": [],
            "site": {
                "id": 1,
                "name": "All Clouds"
            },
            "type": {
                "id": 1,
                "name": "Kubernetes Cluster"
            },
            "zone": {
                "id": 2,
                "name": "VMware 1",
                "zoneType": {
                    "id": 20
                }
            },
            "workerStats": {
                "usedStorage": 22199021568,
                "maxStorage": 126625677312,
                "usedMemory": 3525748000,
                "maxMemory": 12294791168,
                "usedCpu": 0.0,
                "cpuUsage": 18.043023347854614,
                "cpuUsagePeak": 8.235889673233032,
                "cpuUsageAvg": 6.014341115951538
            },
            "config": {}
        },
        {
            "id": 6,
            "name": "Test Ubuntu 22.04",
            "code": null,
            "category": null,
            "visibility": "private",
            "description": "70615",
            "location": null,
            "enabled": true,
            "serviceUrl": null,
            "serviceHost": null,
            "servicePath": null,
            "serviceHostname": null,
            "servicePort": 22,
            "serviceUsername": null,
            "servicePassword": null,
            "servicePasswordHash": null,
            "serviceToken": null,
            "serviceTokenHash": null,
            "serviceAccess": null,
            "serviceAccessHash": null,
            "serviceCert": null,
            "serviceCertHash": null,
            "serviceVersion": null,
            "searchDomains": null,
            "enableInternalDns": false,
            "internalId": null,
            "externalId": null,
            "datacenterId": null,
            "status": "ok",
            "statusDate": "2023-06-13T12:01:15Z",
            "statusMessage": null,
            "inventoryLevel": "full",
            "lastSync": "2023-06-13T12:01:14Z",
            "nextRunDate": "2023-06-13T12:06:15Z",
            "lastSyncDuration": 1028,
            "dateCreated": "2023-06-09T09:50:12Z",
            "lastUpdated": "2023-06-13T12:01:15Z",
            "managed": true,
            "labels": [],
            "serviceEntry": null,
            "createdBy": {
                "id": 1,
                "username": "admin"
            },
            "userGroup": null,
            "layout": {
                "id": 233,
                "name": "Docker Ubuntu 22.04",
                "provisionTypeCode": "vmware"
            },
            "owner": {
                "id": 1,
                "name": "Neo"
            },
            "servers": [
                {
                    "id": 34,
                    "name": "Test Ubuntu 22.04-worker",
                    "typeSet": {
                        "id": 469,
                        "code": "32a2276e-8bfe-4a3a-a37e-06964a6ebd05-c6804b38-e148-4d60-9651-906a210058cf",
                        "name": "Docker Ubuntu 22.04-worker-c6804b38-e148-4d60-9651-906a210058cf-set"
                    },
                    "computeServerType": {
                        "id": 106,
                        "code": "vmwareLinux",
                        "nodeType": "morpheus-node"
                    }
                }
            ],
            "accounts": [],
            "integrations": [],
            "site": {
                "id": 3,
                "name": "Internal"
            },
            "type": {
                "id": 2,
                "name": "Docker Cluster"
            },
            "zone": {
                "id": 2,
                "name": "VMware 1",
                "zoneType": {
                    "id": 20
                }
            },
            "workerStats": {
                "usedStorage": 0,
                "maxStorage": 21474836480,
                "usedMemory": 628036000,
                "maxMemory": 2035904512,
                "usedCpu": 0.0,
                "cpuUsage": 0.36838650703430176,
                "cpuUsagePeak": 0.36838650703430176,
                "cpuUsageAvg": 0.36838650703430176
            },
            "config": {}
        }
    ],
    "meta": {
        "offset": 0,
        "max": 25,
        "size": 2,
        "total": 2
    }
}

module.exports = data;