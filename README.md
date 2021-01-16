##Open Targets 

This programme is to retrieve potential drug targets (protein, protein complex or RNA molecules)
and their correspondinng association scores, and a min/max/average and standard deviation of all associations to a drug or target are returned.




Assumes you have python 3 installed - [https://www.python.org/downloads/]


From CMD line - 

```apt install python-pip```

```pip install opentargets```

Either clone these files from github or just download and save in a folder eg. openTargets 

```git clone https://github.com/sarahjeeeze/openTargets```

```cd openTargets```

run the tests to check it is set up correctly

```python tests.py```

Main programme 


Format to run search for disease of target - 

python openTargetsEMBL.py [-t/-d] [searchTerm]

-t     Target association search,
-d     Disease association search,
--help Returns doc string

Examples - 

```python openTargetsEMBL.py -d alpers```
```python openTargetsEMBL.py -t ENSG00000264781```
```python openTargetsEMBL.py --help```

If input is incorrect you should receive an error message eg.

```Disease not found in database, please check input and try again```
```Incorrect entry must define -t for target or -d for disease```





