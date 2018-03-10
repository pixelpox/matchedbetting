bookMakers = []
openTag = "<span class=\"rlbText\">"
closingTag = "</span>"

rawFile = open("oddsmonkey-test-dump.html", "r") #opens file with name of "test.txt"
for line in rawFile:
	cleanLine = line.strip()
	if cleanLine.startswith(openTag):
		cleanLine = cleanLine.replace(openTag , '')
		cleanLine = cleanLine.replace(closingTag , '')
		
		bookMakers.append(cleanLine)
		
		
		
print bookMakers

BookieFile = open('bookMakers.txt' , 'w')

for bookMaker in bookMakers:
	BookieFile.write(bookMaker + "\n")