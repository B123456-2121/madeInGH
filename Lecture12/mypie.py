#!/usr/bin/python3
for bin_lower in list(range(100,1000,100)) :
    bin_upper = bin_lower + 99
    bin_directory_name = str(bin_lower) + '_' + str(bin_upper)
    shutil.rmtree(bin_directory_name)
    os.mkdir(bin_directory_name)


# create a variable to hold an arbitrary sequence identifier number
seq_number = 1

# Go through each file in the directory
for file_name in os.listdir('dna_files') :
# Check if the file name ends with .dna
  if file_name.endswith('.dna') :
    print('Reading sequences from ' + file_name)
# Open the file and process each line
    dna_file = open('dna_files/' + file_name)
    for line in dna_file :
# Calculate the sequence length
      dna = line.rstrip('\n')
      length = len(dna)
      print('\tsequence length is ' + str(length))
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) :
        bin_upper = bin_lower + 99
        if length >= bin_lower and length <= bin_upper :
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper))
          bin_directory_name = str(bin_lower) + '_' + str(bin_upper)
          output_path = bin_directory_name + '/' + str(seq_number) + '.dna'
          output = open(output_path, 'w')
          output.write(dna)
          output.close()
# Increment the sequence number
          seq_number = seq_number+1
