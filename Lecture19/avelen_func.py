# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 3, 22 Nov 2022
#

# Set up a list object to hold the outputs all the session's searches
search_results = []

# Function with three arguments: taxonomic group (text, not taxid), gene name, number to return)
# NOTE_incomplete: could add another argument to cater for DNA or protein database search?
# NOTE_incomplete: could add another argument to cater for user email address?
def get_average_length(taxonomy, gene, howmany=10):
    from Bio import Entrez, SeqIO
    import os, subprocess
    Entrez.email = "s123456@ed.ac.uk"
    Entrez.api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode()
    search_term = taxonomy + " " + gene + " complete"
# Set up output file, named after search used (spaces removed!)
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retmax=howmany)
    result = Entrez.read(mysearch)
    loopcounter = total_length = 0
# Extract info from the results of the search
    for accession in result['IdList']:
      loopcounter += 1
      gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
      record = SeqIO.read(gb_file, "genbank")
      total_length =  total_length + len(record.seq)
# Add the results of the search to search_results
      search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
# Show the results (trimmed sequence) of the search to screen as we go
      print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
# Write results to search output file
      search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
# Interim print statment for mean length
    mean_length = int(total_length/loopcounter)
    return print(("\nThe mean length was "+str(mean_length)+" amino acids.\n"))
    close(search_output)

get_average_length('Nematoda', 'COX1')
get_average_length('Mammalia', 'COX1')
get_average_length('Arthropoda', 'ATP6')

# What does search_results contain?
for finds in search_results :
  print(finds)



# How about the files we made (1 for each get_average_length() search)?
import os, glob
os.listdir()
sorted(glob.glob("*outputs.txt"))

# Let have a quick look at one of them!
print(open("Nematoda_COX1_complete_outputs.txt").read().strip("\n"))


