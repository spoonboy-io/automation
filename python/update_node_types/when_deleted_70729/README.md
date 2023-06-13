## Update Node Types when deleted

Morpheus Python 3 script which provides interim workaround for 70729.

This script works with synced virtual images which conform to the Azure shared compute 
image gallery specification.

Script reattaches lost virtual image to the node type by maintaining state
(previous good response) in a file cache.