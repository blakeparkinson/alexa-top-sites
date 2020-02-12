with open('merged.csv','r') as in_file, open('deduped.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line not in seen: 
            seen.add(line)
            out_file.write(line)