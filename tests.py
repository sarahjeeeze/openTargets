#!/usr/bin/env python3
"""
Program:    tests
File:       tests.py

Version:    V1.0
Date:       16.01.2021
Function:   Test open targets EMBL python programme

Author:     Sarah Griffiths 

This program is released under the GNU Public Licence

--------------------------------------------------------------------------"""
import unittest
from openTargetsEMBL import targetRetrieve
from openTargetsEMBL import diseaseRetrieve
import sys



class TestTarget(unittest.TestCase):
    
    
    def test_target(self):
        """
            Test for retrival of data by using provided seach term and checking result for maximum is correct

            """
        searchterm = 'ENSG00000073756'
        result = targetRetrieve(searchterm)['Maximum']
        print(result)
   
        self.assertEqual(result,'1.0')
    def test_target2(self):
        """
            Test for retrival of data by using provided seach term and checking result for maximum is correct

            """
        searchterm = 'ENSG00000197386'
        result = targetRetrieve(searchterm)['Average']
        print(result)
   
        self.assertEqual(result,'0.22770631865626045')



    def test_disease(self):
        """
            Test for retrival of data by using provided seach term and checking number of results returned is correct

            """
        searchterm="alpers"
        result = diseaseRetrieve(searchterm)['standard Deviation']

     
        self.assertEqual(result,'0.2383455324940142')
        
    def test_disease2(self):
        """
            Test for retrival of data by using provided seach term minimum is correct

            """
        searchterm="Orphanet_399"
        result = diseaseRetrieve(searchterm)['minimum']

     
        self.assertEqual(result,'0.004')

 
if __name__ == "__main__":
    unittest.main()
