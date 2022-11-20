# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 1, 22 Nov 2022
# Import the required modules
from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email = "s123456@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode()
# Define and do the search
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))
result

# Extract info from the results of the search
count=1
for accession in result['IdList']:
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    print(count,record.id+"\t"+record.description+"\t"+record.seq)
    count += 1
    if count == 6 :
      break

# What were the dictionary keys again?!
result.keys()

print("There were "+str(result['Count'])+" records found.")

