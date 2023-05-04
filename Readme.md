central server :

kadtest.py




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


| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| -------- | -------- | -------- | -------- | -------- |
| Row 1, Column 1 | Row 1, Column 2 | Row 1, Column 3 | Row 1, Column 4 | Row 1, Column 5 |
| Row 2, Column 1 | Row 2, Column 2 | Row 2, Column 3 | Row 2, Column 4 | Row 2, Column 5 |
| Row 3, Column 1 | Row 3, Column 2 | Row 3, Column 3 | Row 3, Column 4 | Row 3, Column 5 |
| Row 4, Column 1 | Row 4, Column 2 | Row 4, Column 3 | Row 4, Column 4 | Row 4, Column 5 |
| Row 5, Column 1 | Row 5, Column 2 | Row 5, Column 3 | Row 5, Column 4 | Row 5, Column 5 |
