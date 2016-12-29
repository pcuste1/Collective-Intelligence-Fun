def getwordcounts(filename):
    text = open(filename, "r")
    
    wc = {}

    for line in text:
        line = line.strip().split()
        if line[0] == "spam": 
            s = 0
        else: 
            s = 1

        for word in line[1:]:
            #word = word.
            wc.setdefault(word, [0,0,0]) 
            wc[word][s] += 1 # Spam or Not occurances 
            wc[word][2] += 1 # Total occurances
            
    return wc

def average(split):
    wc = {}

    for word in split:
        wc[word] = (split[word][0] - split[word][1])#/float(split[word][2])
        
    return wc

def createDataSet(readfile='SMSSpamCollection', writefile='spam.txt'):
    wc = getwordcounts(readfile)
    outfile = open(writefile, 'w')
    outfile.write(writefile+'\tDIFF\n')
    for key in wc:
        if wc[key][2] < 50: continue 
        outfile.write(key + '\t' + str((wc[key][0] - wc[key][1]) / wc[key][2])
                      + '\n')
    
