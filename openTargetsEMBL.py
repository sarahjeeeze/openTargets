#!/usr/bin/env python3
"""
Program:    openTargets
File:       openTargets.py

Version:    V1.0
Date:       16.01.2021
Function:   Obtain open Targets association scores for targets and diseases


Author:     Sarah Griffiths 

This program is released under the GNU Public Licence (GPL V3)

--------------------------------------------------------------------------
Description:
============
This is a programme that can be access from command line to return a list of
targets or diseases from the open targets database with their association scores,
It then calculates and prints to the stdout the average(mean),standard deviation
and min/max.

Usage:

python openTargetsEMBL.py [-t/-d] [searchTerm]

-t     Target association search,
-d     Disease association search,
--help Returns doc string

Revision History:
=================
V1.0   16.01.2021   Original   By: SG
"""
#*************************************************************************

import opentargets 
import statistics 
import sys


ot = opentargets.OpenTargetsClient()

def targetRetrieve(x):
    """function for retrieving target association scores
    INPUT: target ID
    OUTPUT: all associated target ID's and their overall association scores, Max, Min, Average and Standard deviation returned as a dictionary"""
    target = str(x)
    a_for_target = ot.get_associations_for_target(target)
    allscores = []
    for a in a_for_target:
         
        score = a['association_score']['overall']
        print(a['id'], a['association_score']['overall'])
        allscores.append(score)
    stats = {'Maximum': str(max(allscores)),'Minimum' : str(min(allscores)), 'Average' : str(statistics.mean(allscores)),'standard Deviation' : str(statistics.stdev(allscores))}
    return(stats)



def diseaseRetrieve(x):
    """function for retrieving target association scores
    INPUT: Disease name 
    OUTPUT: all associated disease ID's and their overall association scores, Max, Min, Average and Standard deviation"""
    disease = str(x)
    a_for_target = ot.get_associations_for_disease(disease)

    allscores = []
   
    for a in a_for_target:
        
        score = a['association_score']['overall']
        print(a['id'], a['association_score']['overall'])
        allscores.append(score)
   
    stats = {'maximum': str(max(allscores)),
             'minimum' : str(min(allscores)),
             'Average' : str(statistics.mean(allscores)),
             'standard Deviation' : str(statistics.stdev(allscores))
             }
    return(stats)
    
    

    
if __name__ == "__main__":
    

    if len(sys.argv)==2 and sys.argv[1]=='--help':
        print(__doc__)

 

    elif (sys.argv[1]) == '-t':
        searchTerm = str(sys.argv[2])
        try:
            #targetRetrieve(searchTerm)
            ot.get_associations_for_target(searchTerm)
            a = targetRetrieve(searchTerm)
            for k,v in a.items():
               print(k,':',v)
        except ValueError as err: 
            print('Target not found in database, please check input and try again')
        except StopIteration as err:
            print('Target not found in database, please check input and try again')
            
        
    elif (sys.argv[1]) == '-d':
        searchTerm = str(sys.argv[2])
        try:
            diseaseRetrieve(searchTerm)
            a = diseaseRetrieve(searchTerm)
            for k,v in a.items():
                print(k,':',v)
            
        except ValueError as err: 
            print('Disease not found in database, please check input and try again')
        except StopIteration as err:
            print('Disease not found in database, please check input and try again')
    else:
        print('Incorrect entry must define -t for target or -d for disease  \n example: python embl.py -t ENSG00000197386')



