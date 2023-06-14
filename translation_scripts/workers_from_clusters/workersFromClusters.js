// some development/test data
let data = require("./data")

// emulate a dependent input
let input = {};
input.clusterID = 3

/**** TRANSLATION SCRIPT STARTS HERE ****/

// assumes input which provides cluster id is called clusterID)
let results = [];
let clusters = data["clusters"] ;
for(let i = 0; i < clusters.length; i++){
    if (clusters[i]["id"] === input.clusterID) {
        // we've matched our cluster
        let servers = clusters[i]["servers"];
        for (let i2 = 0; i2 < servers.length; i2++) {
            // iterate the servers (master and workers)
        
            if(servers[i2]["computeServerType"]["nodeType"] === "kube-worker"){
                // its a worker build data for select
                let workerName = servers[i2]["name"];
                let workerId = servers[i2]["id"];
                results.push({name: workerName,value: workerId});
            }
        }
    }
}

/**** TRANSLATION SCRIPT ENDS HERE ****/

// for dev only
console.log(results);