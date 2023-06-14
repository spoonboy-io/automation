// Dev/Test data - snapshot of return from the Morpheus API
let data = {
    "instances": [
        {
            "id": 3,
            "uuid": "518723ad-ec0b-4bd3-bb1c-326531757f71",
            "accountId": 1,
            "tenant": {
                "id": 1,
                "name": "Neo"
            },
            "instanceType": {
                "id": 9,
                "code": "ubuntu",
                "category": "os",
                "name": "Ubuntu",
                "image": "/assets/branding/140x40/ubuntu.svg"
            },
            "group": {
                "id": 1,
                "name": "All Clouds"
            },
            "cloud": {
                "id": 1,
                "name": "Nutanix 1",
                "type": "nutanix"
            },
            "containers": [
                3
            ],
            "servers": [
                4
            ],
            "resources": [],
            "connectionInfo": [
                {
                    "ip": "10.32.20.161",
                    "port": 22,
                    "name": "SSH"
                }
            ],
            "layout": {
                "id": 1073,
                "name": "Nutanix VM",
                "provisionTypeId": 31,
                "provisionTypeCode": "nutanix"
            },
            "plan": {
                "id": 129,
                "code": "nutanix-vm-1024",
                "name": "1 vCPU, 1GB Memory"
            },
            "name": "Webserver-lin-01",
            "description": null,
            "environment": "dev",
            "config": {
                "isVpcSelectable": true,
                "isEC2": false,
                "resourcePoolId": "",
                "createUser": false,
                "expose": [],
                "noAgent": true,
                "customOptions": {},
                "createBackup": true,
                "memoryDisplay": "MB",
                "backup": {
                    "veeamManagedServer": "",
                    "createBackup": false,
                    "jobAction": "new",
                    "jobRetentionCount": 3
                },
                "layoutSize": 1,
                "lbInstances": []
            },
            "configGroup": null,
            "configId": null,
            "configRole": null,
            "volumes": [
                {
                    "controllerId": null,
                    "datastoreId": "2",
                    "displayOrder": 0,
                    "id": 45,
                    "uuid": "aa29f103-e544-4599-8f15-b8645f95f10a",
                    "maxIOPS": null,
                    "maxStorage": 10737418240,
                    "name": "root",
                    "shortName": "root",
                    "resizeable": true,
                    "planResizable": true,
                    "rootVolume": true,
                    "size": 10,
                    "storageType": 48,
                    "unitNumber": "0",
                    "controllerMountPoint": null
                }
            ],
            "controllers": [],
            "interfaces": [
                {
                    "id": "network-2",
                    "network": {
                        "id": 2,
                        "group": null,
                        "subnet": null,
                        "dhcpServer": true,
                        "name": "VLAN 2 Internal server network",
                        "pool": null
                    },
                    "ipAddress": null,
                    "networkInterfaceTypeId": null,
                    "ipMode": ""
                }
            ],
            "customOptions": {},
            "instanceVersion": "22.04",
            "labels": [],
            "tags": [],
            "evars": [
                {
                    "name": "UBUNTU_IP",
                    "value": "10.32.20.161",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_HOST",
                    "value": "container3",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_SSH",
                    "value": 22,
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_PORT",
                    "value": 22,
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_PROTO",
                    "value": "tcp",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_ADDR",
                    "value": "10.32.20.161",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP",
                    "value": "tcp://10.32.20.161:22",
                    "export": true,
                    "masked": false
                }
            ],
            "maxMemory": 1073741824,
            "maxStorage": 10737418240,
            "maxCores": 1,
            "coresPerSocket": 1,
            "maxCpu": null,
            "hourlyCost": 0.0,
            "hourlyPrice": 0.0,
            "instancePrice": {
                "price": 0E-9,
                "cost": 0E-9,
                "currency": "GBP",
                "unit": "month"
            },
            "dateCreated": "2023-05-09T16:43:28Z",
            "lastUpdated": "2023-06-14T08:00:06Z",
            "hostName": "dummytechservice-01",
            "domainName": null,
            "environmentPrefix": null,
            "firewallEnabled": true,
            "networkLevel": "container",
            "autoScale": false,
            "instanceContext": "dev",
            "currentDeployId": null,
            "locked": false,
            "status": "running",
            "statusMessage": null,
            "errorMessage": null,
            "statusDate": "2023-05-09T16:44:38Z",
            "statusPercent": null,
            "statusEta": null,
            "userStatus": null,
            "expireDays": null,
            "renewDays": null,
            "expireCount": 0,
            "expireDate": null,
            "expireWarningDate": null,
            "expireWarningSent": false,
            "shutdownDays": null,
            "shutdownRenewDays": null,
            "shutdownCount": 0,
            "shutdownDate": null,
            "shutdownWarningDate": null,
            "shutdownWarningSent": false,
            "removalDate": null,
            "createdBy": {
                "id": 1,
                "username": "admin"
            },
            "owner": {
                "id": 1,
                "username": "admin"
            },
            "notes": null,
            "stats": {
                "usedStorage": 3345049600,
                "maxStorage": 10737418240,
                "usedMemory": 823992320,
                "maxMemory": 1073741824,
                "usedCpu": 0.004153,
                "cpuUsage": 0.004153,
                "cpuUsagePeak": 0.004153,
                "cpuUsageAvg": 0.004153
            },
            "powerSchedule": null,
            "isScalable": true,
            "instanceThreshold": null,
            "isBusy": false,
            "apps": []
        },
        {
            "id": 2,
            "uuid": "16e528e1-7978-49d8-aa5c-9a20fa1e25eb",
            "accountId": 1,
            "tenant": {
                "id": 1,
                "name": "Neo"
            },
            "instanceType": {
                "id": 9,
                "code": "ubuntu",
                "category": "os",
                "name": "Ubuntu",
                "image": "/assets/branding/140x40/ubuntu.svg"
            },
            "group": {
                "id": 1,
                "name": "All Clouds"
            },
            "cloud": {
                "id": 1,
                "name": "Nutanix 1",
                "type": "nutanix"
            },
            "containers": [
                2
            ],
            "servers": [
                3
            ],
            "resources": [],
            "connectionInfo": [
                {
                    "ip": "10.32.20.16",
                    "port": 22,
                    "name": "SSH"
                }
            ],
            "layout": {
                "id": 1073,
                "name": "Nutanix VM",
                "provisionTypeId": 31,
                "provisionTypeCode": "nutanix"
            },
            "plan": {
                "id": 129,
                "code": "nutanix-vm-1024",
                "name": "1 vCPU, 1GB Memory"
            },
            "name": "Tab2",
            "description": null,
            "environment": "dev",
            "config": {
                "isVpcSelectable": true,
                "isEC2": false,
                "resourcePoolId": "",
                "createUser": false,
                "expose": [],
                "noAgent": true,
                "customOptions": {},
                "createBackup": true,
                "memoryDisplay": "MB",
                "backup": {
                    "veeamManagedServer": "",
                    "createBackup": false,
                    "jobAction": "new",
                    "jobRetentionCount": 3,
                    "providerBackupType": -1
                },
                "layoutSize": 1,
                "lbInstances": []
            },
            "configGroup": null,
            "configId": null,
            "configRole": null,
            "volumes": [
                {
                    "controllerId": null,
                    "datastoreId": "2",
                    "displayOrder": 0,
                    "id": 44,
                    "uuid": "44fe9b81-6286-4603-9b1b-c80582c6ef92",
                    "maxIOPS": null,
                    "maxStorage": 10737418240,
                    "name": "root",
                    "shortName": "root",
                    "resizeable": true,
                    "planResizable": true,
                    "rootVolume": true,
                    "size": 10,
                    "storageType": 48,
                    "unitNumber": "0",
                    "controllerMountPoint": null
                }
            ],
            "controllers": [],
            "interfaces": [
                {
                    "id": "network-2",
                    "network": {
                        "id": 2,
                        "group": null,
                        "subnet": null,
                        "dhcpServer": true,
                        "name": "VLAN 2 Internal server network",
                        "pool": null
                    },
                    "ipAddress": null,
                    "networkInterfaceTypeId": null,
                    "ipMode": ""
                }
            ],
            "customOptions": {},
            "instanceVersion": "22.04",
            "labels": [],
            "tags": [],
            "evars": [
                {
                    "name": "UBUNTU_IP",
                    "value": "10.32.20.16",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_HOST",
                    "value": "container2",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_SSH",
                    "value": 22,
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_PORT",
                    "value": 22,
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_PROTO",
                    "value": "tcp",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP_ADDR",
                    "value": "10.32.20.16",
                    "export": true,
                    "masked": false
                },
                {
                    "name": "UBUNTU_PORT_22_TCP",
                    "value": "tcp://10.32.20.16:22",
                    "export": true,
                    "masked": false
                }
            ],
            "maxMemory": 1073741824,
            "maxStorage": 10737418240,
            "maxCores": 1,
            "coresPerSocket": 1,
            "maxCpu": null,
            "hourlyCost": 0.0,
            "hourlyPrice": 0.0,
            "instancePrice": {
                "price": 0E-9,
                "cost": 0E-9,
                "currency": "GBP",
                "unit": "month"
            },
            "dateCreated": "2023-05-05T14:03:10Z",
            "lastUpdated": "2023-06-14T08:00:06Z",
            "hostName": "tab2",
            "domainName": null,
            "environmentPrefix": null,
            "firewallEnabled": true,
            "networkLevel": "container",
            "autoScale": false,
            "instanceContext": "dev",
            "currentDeployId": null,
            "locked": false,
            "status": "running",
            "statusMessage": null,
            "errorMessage": null,
            "statusDate": "2023-05-05T14:04:38Z",
            "statusPercent": null,
            "statusEta": null,
            "userStatus": null,
            "expireDays": null,
            "renewDays": null,
            "expireCount": 0,
            "expireDate": null,
            "expireWarningDate": null,
            "expireWarningSent": false,
            "shutdownDays": null,
            "shutdownRenewDays": null,
            "shutdownCount": 0,
            "shutdownDate": null,
            "shutdownWarningDate": null,
            "shutdownWarningSent": false,
            "removalDate": null,
            "createdBy": {
                "id": 1,
                "username": "admin"
            },
            "owner": {
                "id": 1,
                "username": "admin"
            },
            "notes": "charset=ISO-8859-1 works for encoding german special chars: Ü Ö ä ö ü ß ?",
            "stats": {
                "usedStorage": 3359808000,
                "maxStorage": 10737418240,
                "usedMemory": 773726208,
                "maxMemory": 1073741824,
                "usedCpu": 0.003716,
                "cpuUsage": 0.003716,
                "cpuUsagePeak": 0.003716,
                "cpuUsageAvg": 0.003716
            },
            "powerSchedule": null,
            "isScalable": true,
            "instanceThreshold": null,
            "isBusy": false,
            "apps": []
        }
    ],
    "meta": {
        "offset": 0,
        "max": 25,
        "size": 2,
        "total": 2
    }
};

module.exports = data;