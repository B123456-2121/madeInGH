# Import the module
import re

# INPUT list of accessions
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']


# INPUT list of accessions
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']

outputs = []

# PROCESS list of accessions
for acc in accessions: 
# contain the number 5 (could also do if '5' in acc :)
    if re.search(r'5', acc) : 
        outputs.append('contain the number 5: ' + acc)
# contain the letter d or e
    if re.search(r'[de]', acc) : 
        outputs.append('contain the letter d or e: ' + acc)
# contain the letters d and e (adjacent)
    if re.search(r'de', acc) : 
        outputs.append('contain the letter d and e (have to be adjacent): ' + acc)
# contain the letters d and e in that order (dont have to be adjacent, but can be)
    if re.search(r'd.*e', acc) : 
        outputs.append('contain the letter d and e in that order (dont have to be adjacent): ' + acc)
# contain the letters d and e in that order with a single letter between them
    if re.search(r'd.e', acc) : 
        outputs.append('contain the letter d and e in that order with a single letter between them: ' + acc)
# contain both the letters d and e in any order
    if re.search(r'd', acc) and re.search(r'e', acc) : 
        outputs.append('contain both the letters d and e in any order: ' + acc)
# start with x or y
# could have used if acc.startswith('x') or acc.startswith('y') :
# could have used if re.search(r'^[xy]', acc) :
    if re.search(r'(^x|^y)', acc) : 
        outputs.append('start with x or y: ' + acc)
# start with x or y and end with e
# could have used if (acc.startswith('x') or acc.startswith('y')) and acc.endswith('e') :
# could have used if re.search('(^x|^y).+e$',acc) :
# could have used if re.search('"[xy].+e$',acc) :
    if re.search(r'(^x|^y)', acc) and re.search(r'(e$)', acc) : 
        outputs.append('start with x or y and end with e: ' + acc)
# contains any 3 numbers in any order
    if len(re.findall(r'\d',acc)) == 3 :
        outputs.append('contains any 3 numbers in any order: ' + acc)
# contains 3 different numbers
    if len(set(re.findall(r'\d',acc))) == 3 :
        outputs.append('contains 3 different numbers: ' + acc)
# contain three or more numbers in a row
# could have used if re.search(r'[0123456789]{3,}', acc) :
    if re.search(r'\d{3,}', acc): 
        outputs.append('contain three or more numbers in a row: ' + acc)
# end with d then either a, r or p
    if re.search(r'd[arp]$', acc): 
        outputs.append('end with d followed by either a, r or p: ' + acc)

outputs.sort()
print(('\n').join(outputs))




dna = open('/localdisk/data/BPSM/Lecture17/long_dna.txt').read().rstrip('\n')
len(dna)
2012

# This goes WAY off the screen...!
dna
'ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT'


# Cool way to make the long string look nicer printed on the screen...

print("\n".join(re.findall('.{1,60}', dna)))

ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCG
GCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGG
GTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAA
GAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGC
GGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGC
TATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGC
CTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAG
TGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGC
GAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGAC
TAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAAC
GTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCT
AGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCG
GCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACG
GGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCT
GGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAG
CGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTAT
TGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGA
ACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCG
CAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGG
ATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACC
TAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCG
TGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTC
AATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGG
CTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAA
ACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCA
TATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCG
CCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTC
GCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGA
GGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGA
AATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACG
TTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCC
GTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGA
GCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAG
TACCAGAGAAGATGACTACTGAGTTGTGCGAT


BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:',BpsmI) 

# Find the sites, incrementing by three to account for where the enzyme cuts in the recognition sequence

for matching in re.finditer(BpsmI, dna): 
    print(matching.start()+3) 


# Start: open and read the file

dna = open('/localdisk/data/BPSM/Lecture17/long_dna.txt').read().rstrip('\n') 
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position = matching.start() + 3
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))


# First, define both enzymes sites

BpsmI='A[GATC]TAAT'

BpsmII='GC[AG][AT]TG'



# Make a list to store the cut positions for both enzymes

all_cuts = []


# Add cut positions for BpsmI 

for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3) 


# Add cut positions for BpsmII

for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

print(all_cuts)


# These aren't in sequential order, so just sort them

all_cuts.sort()

all_cuts

# Double digest run

last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position

# Now the last fragment

fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

# We have just worked out where the enzymes cut the DNA sequence,

# so all we need to do is to use the cut positions as index positions to

# substring the dna sequence string!




# Let's use a dictionary to store the fragment sequences


fragment_sequences = {} 

# Double digest run

last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )

# Get the sequence substring

    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])

# Get the fragment start and end
    
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position

# Now the last fragment

fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)



# Show all the sequences

print(('\n########\n').join(list(fragment_sequences.values())))
# Are the fragments actually adjacent?  Quick check!

# End of Fragment 1 ACGCGT should be next to 

# beginning of Fragment 2 TGAACA

# so lets use ACGCGTTGAACA as a query against our sequence

re.search(r'ACGCGTTGAACA',dna)



