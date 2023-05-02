



## To Run, use the below command

    python3 <N> <Base port 1> <Base Port 2>

 - N -> Number of Nodes 
 - Base Port 1 -> Port Number at which Kademlia
   Nodes will start 
 - Base Port 2 -> Port Number at which HTTP servers of    nodes will
   start

## Example

    python3 5 8000 9000

The above command creates 5 node kademlia DHT with node servers set up from port 8000 and HTTP servers set up from port 9000

## HTTP APIs

 - localhost:<httpport>/get/< key >
 - localhost:<httpport>/set/< key >/< value >
 - localhost:<httpport>/< file >/< filename >



## Report and ppt
Report : https://www.overleaf.com/project/63e0323d40d9ac119b72cbc9

slides: https://docs.google.com/presentation/d/1ACowhPyiXjJyBREm-huRKVQ9gyt8OOgd7PWM8goPOPk/edit?usp=sharing