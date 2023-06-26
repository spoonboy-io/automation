let data =  require("./data-sources/cloud-matrix.js");

// fake selected region id
let input = [];

input.azSite = 1;
input.azEnvironment = 1;
input.azServerType = 1;

/**** TRANSLATION SCRIPT STARTS HERE ****/

// region translation script
results = [];
for (let i=0; i < data.length; i++){
    if ((input.azSite == data[i].siteId) && (input.azEnvironment == data[i].envId) && (input.azServerType == data[i].serverTypeId)){
        results.push({name: data[i].name, value:data[i].id});
    }
}

/**** TRANSLATION SCRIPT ENDS HERE ****/

console.log(results);