// some development/test data
let data = require("./data")

/**** TRANSLATION SCRIPT STARTS HERE ****/

let filterTerm = "lin"; // for linux

let results = [];
let instances = data["instances"];
for(let i=0; i< instances.length; i++) {
    if (instances[i].name.toLowerCase().includes(filterTerm)) {
        results.push({name: instances[i].name, value: instances[i].id});
    }
}

/**** TRANSLATION SCRIPT ENDS HERE ****/

// for dev only
console.log(results);