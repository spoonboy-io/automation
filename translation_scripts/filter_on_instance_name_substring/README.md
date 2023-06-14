## Filter on instance name substring

Extracts instances with a matching substring from all instances (case insenstive).
E.g. Show only linux instances, assuming "lin" is applied in the name via a policy

### Why?

[Discuss Link](https://discuss.morpheusdata.com/t/option-lists-morpheus-api/1187)

### Run/test locally

```node
node filterOnInstanceNameSubstring.js
```

### Sample response

Data for a select input, dependent on cluster selected.

```
// filtered on 'lin'
[ 
    { name: 'Webserver-lin-01', value: 2 } 
]
```