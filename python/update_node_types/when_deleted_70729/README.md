## Update Node Types when deleted

Morpheus Python 3 script which provides interim workaround for 70729.

This script works with synced virtual images which conform to the Azure shared compute 
image gallery specification.

### Usage

The script works by creating a cache of a good state. On each API call if nodes with null virtual image are found, 
the cache is consulted to find what virtual image should be attached. The node is then updated over the API.

Before implementing node types should have their virtual images manually reattached so this good state can be 
stored in the cache.

### Important 

The `testMode=True` (line 19). This script can be run in this mode to see what updates will
be made, without them being made. When happy script is applying the expected updates set this to `False`.

There is `debugMode=True` (line 22) which provides more verbose output about skipped images.

The `excludeNodeTypeList = [5, 333]` (line 43). Use this array to ignore any system node types with null virtual images
If nulls are detected and they are not in this array, the cache will not be built.

Script reattaches virtual image to the node type by maintaining state
(previous good response) in a file cache. The name of the image found in the cached data is used to identify the new synced image
in the virtual images api call and attach that to the node type.