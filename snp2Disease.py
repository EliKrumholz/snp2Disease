#! /usr/bin/env python

def snp2Disease(snpLocs, snpDB, snp2omimDB, omimDB):
    # Maps SNP locations to diseases. 
    # snpLocs is a 2 by n array, with snpLocs[0][i] = chromosome number
    # and snpLocs[1][i] = chromosome location (nucleotide location)

    snpMatching = {'matchedSNPs': {}, 'noOmimSNPs': {}, 'noRsSNPs': {}}
    for i in range(1,25):
        snpMatching['matchedSNPs'][i] = {}
        snpMatching['noOmimSNPs'][i] = []
        snpMatching['noRsSNPs'][i] = []

    for snpLoc in snpLocs:
        try:
            rsId = snpDB[snpLoc[0]][snpLoc[1]]
        except KeyError:
            snpMatching['noRsSNPs'][snpLoc[0]].append(snpLoc[1])
            continue

        try:
            omimId = snp2omimDB[rsId]
        except KeyError:
            snpMatching['noOmimSNPs'][snpLoc[0]].append(snpLoc[1])
            continue

        try:
            disease = omimDB[omimId]
        except KeyError:
            print 'Missing disease for %s' % omimId
            continue

        snpMatching['matchedSNPs'][snpLoc[0]][snpLoc[1]] = disease

    return snpMatching


def loadDBs(snpDBPath, snp2omimDBPath, omimDBPath):
    # Load snpDB, this can be downloaded from:
    # ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/chr_rpts/
    # Files can be appended to include multiple chromosomes.
    
    snpDB = {}
    for i in range(1,25):
        snpDB[i] = {}

    for line in open(snpDBPath):
        values = line.rstrip('\n').split('\t')
        try:
            snpDB[int(values[6])][int(values[11])] = int(values[0])
        except ValueError:
            pass

    # Load snp2omimDB, this can be downloaded from:
    # ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/database/organism_data/OmimVarLocusIdSNP.bcp.gz
    
    snp2omimDB = {}
    for line in open(snp2omimDBPath):
        values = line.rstrip('\n').split('\t')
        try:
            snp2omimDB[int(values[8])] = int(values[0])
        except ValueError:
            pass


    # Load omimDB, this can be downloaded from:
    # http://www.omim.org/downloads 
    # Requires registration, the required file is "morbidmap"

    omimDB = {}
    for line in open(omimDBPath):
        values = line.rstrip('\n').split('|')
        try:
            omimDB[int(values[2])] = values[0]
        except IndexError:
            pass

    return snpDB, snp2omimDB, omimDB
