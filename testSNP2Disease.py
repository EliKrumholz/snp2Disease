#! /usr/bin/env python

import snp2Disease 

snpDBPath = '' # Path to chromosome file. I.e. 'chr_1.txt'
snp2OmimDBPath = '' # Path to dbSNP to OMIM file: OmimVarLocusIdSNP.bcp
omimDBPath = '' # Path to OMIM morbidmap file.

# Specifiy the chromosome number for the chromosome file provided.
chromosomeNum =  # Chromosome number for chromosome file. I.e.: 1

# Build database maps.
(snpDB, snp2OmimDB, omimDB) = snp2Disease.loadDBs(snpDBPath, snp2OmimDBPath, omimDBPath)

testSNPs = []

# Test the script with all SNPs from the chromosome file.
for key in enumerate(snpDB[chromosomeNum].keys()):
    testSNPs.append([chromosomeNum, key])

# Match SNPs to diseases.
snpMatching = snp2Disease.snp2Disease(testSNPs, snpDB, snp2OmimDB, omimDB)
