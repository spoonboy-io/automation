let data =  require("./data-sources/site.js");

// fake selected region id
let input = [];
input.azRegion = 1;

/**** TRANSLATION SCRIPT STARTS HERE ****/

// site translation script
results = [];
for (let i=0; i < data.length; i++){
    if(input.azRegion === data[i].regionId){
        results.push({name: data[i].name, value:data[i].id});
    }
}

/**** TRANSLATION SCRIPT ENDS HERE ****/

console.log(results);