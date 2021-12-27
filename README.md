# nwbv2conversion
Conversion of public neurophysiology datasets to NeuroData Without Borders format
Organization:INCF
Description
 The goal of this project is to convert publicly available datasets to the standardized NeuroData Without Borders (NWB) format so that they can be better interpreted and reused by other researchers.
 
The following are the python requirements to implement:
numpy (1.17.2)
pandas (0.23.0)
scipy (1.1.0)
matplotlib (2.2.2)
pynwb (1.1.0)
hdmf (1.2.0)
seaborn (0.9.0)
 ->pynwb-1.1.0 and hdmf-1.2.0 have been strictly used 
 source for data:https://osf.io/cd6qp/
output image:
<img width="347" alt="nwb image" src="https://user-images.githubusercontent.com/63154980/147445559-5cbe956a-5ca3-48a7-b278-da6cad617ae5.png">
issues faced:
->there are few errors in the hr_struct.py and ht_treenode.py on which the work is being done currently.
