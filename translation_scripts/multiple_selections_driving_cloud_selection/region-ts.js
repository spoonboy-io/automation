let data =  require("./data-sources/region.js");

/**** TRANSLATION SCRIPT STARTS HERE ****/

// region translation script
results = [];
for (let i=0; i < data.length; i++){
    results.push({name: data[i].name, value:data[i].id});
}

/**** TRANSLATION SCRIPT ENDS HERE ****/

console.log(results);