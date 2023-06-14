## Extract workers for a cluster

Extracts workers of a Morpheus cluster from the `api/clusters` API response (all clusters). 

### Why?

[Discuss Link](https://discuss.morpheusdata.com/t/option-lists-rest-apis-pass-dynamic-parameter-in-source-url/1186)

### Run/test locally

```node
node workersFromClusters.js
```

### Sample response

Data for a select input, dependent on cluster selected.

```
[
  { name: 'MKS 1-worker-1', value: 14 },
  { name: 'MKS 1-worker-3', value: 16 },
  { name: 'MKS 1-worker-2', value: 15 }
]

```