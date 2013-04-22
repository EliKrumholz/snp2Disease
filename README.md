snp2disease
===========

A simple script to map SNP locations to known OMIM diseases loci.

Usage:
======
Input:
------

To map SNP locations to diseases the user must download several files from online repositories:

1. A chr\_rpts file from ftp://ftp.ncbi.nih.gov/snp/organisms/human\_9606/chr\_rpts/
2. An OmimVarLocusIdSNP.bcp file from ftp://ftp.ncbi.nih.gov/snp/organisms/human\_9606/database/organism\_data/OmimVarLocusIdSNP.bcp.gz
3. A morbidmap file from http://www.omim.org/downloads. This file requires registration to download (and thus why I cannot include the file in the repo.)

SNPs are then passed to the snp2Disease function as a two column array. The first column stores the chromosome number as per dbSNP syntax (1-24), and the second column contains the nucleotide base pair notation of the SNP on the chromosome.


Output:
-------
The function outputs a dictionary with three keys:

1. 'matchedSNPs' : A dictionary of chromosome numbers : A dictionary of chromosome nucleotide locations : A disease description
2. 'noOmimSNPs' : A dictionary of chromosome numbers : A list of chromosome locations with no associated OMIM diseases
3. 'noRsSNPs' : A dictionary of chromosome numbers : A list of chromosome locations with no associated rs identifiers

