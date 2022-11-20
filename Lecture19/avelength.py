# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 2, 22 Nov 2022

# Import the required modules
from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email = "s123456@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode()

# Define and do the search
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))

# Include a counter and a variable to hold the total length
loopcounter = total_length = 0

# Extract info from the results of the search,
# recalculating the mean length as we go
for accession in result['IdList']:
    loopcounter += 1
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    total_length =  total_length + len(record.seq)
    mean_length = int(total_length/loopcounter)
    print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:10]+"...")


# Output some useful info
print("There were "+str(result['Count'])+" records found.")
print("The mean length was "+str(mean_length)+" amino acids.")

