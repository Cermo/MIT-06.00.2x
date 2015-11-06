import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def plotVowelProportionHistogram(wordList, numBins=15):
	"""
	Plots a histogram of the proportion of vowels in each word in wordList
	using the specified number of bins in numBins
	"""
	proportionOfVowels = []
	for word in wordList:
		numOfVowelsInWord = 0
		for char in word:
			if char in "aeiou":
				numOfVowelsInWord += 1
		proportionOfVowels.append(numOfVowelsInWord/float(len(word)))
	mean = sum(proportionOfVowels)/len(proportionOfVowels)
	sd = stdDev(proportionOfVowels)
	
	pylab.hist(proportionOfVowels, bins = 15)
	xmin,xmax = pylab.xlim()
	ymin,ymax = pylab.ylim()
	
	
	pylab.title('Fraction of Vowels in ' + str(len(wordList)) + ' words dictionary')
	pylab.xlabel('Fraction of Vowels')
	pylab.ylabel('Number of words')
	xmin, xmax = pylab.xlim()
	ymin, ymax = pylab.ylim()
	pylab.text(xmin + (xmax-xmin)*0.02, ymax/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))
	pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
