## Open Targets 

This programme is to retrieve potential drug targets (protein, protein complex or RNA molecules) with their correspondinng association scores.
The Minimum, Maximum, Average and standard deviation of all associations are also returned.

## Set up

Assumes you have python 3 installed - https://www.python.org/downloads/

From CMD line - 

```apt install python-pip```

```pip install opentargets```

Either clone these files from github or just download and save in a folder eg. openTargets 

```git clone https://github.com/sarahjeeeze/openTargets```

```cd openTargets```

run the tests to check it is set up correctly

```python tests.py```

## Main programme 

Format to run script - 

python openTargetsEMBL.py [-t/-d/--help] [searchTerm]

-t     Target association search <br />
-d     Disease association search <br />
--help Returns doc string

Examples - 

```python openTargetsEMBL.py -d alpers``` <br />
```python openTargetsEMBL.py -t ENSG00000264781``` <br />
```python openTargetsEMBL.py --help``` <br />

If input is incorrect you should receive an error message eg.

```Disease not found in database, please check input and try again``` <br />
```Incorrect entry must define -t for target or -d for disease```

See sampleOutput folder for example of expected output for Kuru disease



## Reference

Denise Carvalho-Silva, Andrea Pierleoni, Miguel Pignatelli, ChuangKee Ong, Luca Fumis, Nikiforos Karamanis, 
Miguel Carmona, Adam Faulconbridge, Andrew Hercules, Elaine McAuley, Alfredo Miranda, Gareth Peat, Michaela Spitzer,
Jeffrey Barrett, David G Hulcoop, Eliseo Papa, Gautier Koscielny, Ian Dunham, Open Targets Platform: new developments 
and updates two years on, Nucleic Acids Research, Volume 47, Issue D1, 08 January 2019, Pages D1056–D1065, https://doi.org/10.1093/nar/gky1133




