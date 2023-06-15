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

The `testMode=True` (line 14). This script can be run in this mode to see what updates will
be made, without them being made. When happy script is applying the expected updates set this to `False`.

The `excludeNodeTypeList = [5, 333]` (line 33). Use this array to ignore any system node types with null virtual images
If nulls are detected and they are not in this array, the cache will not be built.

Script reattaches lost virtual image to the node type by maintaining state
(previous good response) in a file cache.