import os
import re
import csv
import math

headers1 = ['SearchQuery', 'Documents Containing Term (df)', 'Total Documents (N)/df', 'log10(N/df)']
headers2 = ['Documents', 'Total Words (m)', 'Frequency (f)']

CWordCount = 0
HWordCount = 0
DuWordCount = 0
Uwordcount = 0
Bwordcount = 0
max = 0
rowcount = 0
words = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Business']
pattern = re.compile('|'.join(words))

# This script will consider each article as a document and stored the same in a text file
with open('newsdata.csv', 'r') as csvfile:
    line = csvfile.readlines()
    for row in range(len(line)):
        rowcount = rowcount+1
        file_name = "Article"+str(rowcount)+".txt"
        article = line[row].replace(',','\n')
        with open(os.path.join('C:\\Users\\rocki\PycharmProjects\csv\Semantic',file_name), 'w') as output:
            output.write(article)

#This will count the documents that has these words(i.e.'Canada', 'University', 'Dalhousie University', 'Halifax', 'Business')
with open('semanticA.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(headers1)
    for root, dirs, files in os.walk('C:\\Users\\rocki\\PycharmProjects\\csv\\Semantic'):
        if files:
            for filename in files:
                Total = len(files)
                with open(os.path.join('C:\\Users\\rocki\PycharmProjects\csv\Semantic', filename), 'r') as f:
                    contents = f.read()
                    print(contents)
                    if words[0] in contents:
                        print(words[0] +'found')
                        CWordCount += 1
                    if words[1] in contents:
                        print(words[1] +'found')
                        Uwordcount += 1
                    if words[2] in contents:
                        print(words[2] +'found')
                        DuWordCount += 1
                    if words[3] in contents:
                        print(words[3] +'found')
                        HWordCount += 1
                    if words[4] in contents:
                        print(words[4] +'found')
                        Bwordcount += 1
            csv_writer.writerow([words[0], CWordCount, str(Total)+'/'+str(CWordCount), math.log10(Total/CWordCount)])
            csv_writer.writerow([words[1], Uwordcount, str(Total)+'/'+str(Uwordcount), math.log10(Total/Uwordcount)])
            csv_writer.writerow([words[2], DuWordCount, str(Total)+'/'+str(DuWordCount), math.log10(Total/DuWordCount)])
            csv_writer.writerow([words[3], HWordCount, str(Total)+'/'+str(HWordCount), math.log10(Total/HWordCount)])
            csv_writer.writerow([words[4], Bwordcount, str(Total)+'/'+str(Bwordcount), math.log10(Total/Bwordcount)])
            print(Total)
        else:
            print("Empty Directory")


# #This will calculate the total count of words in a document along with number of occurences of word "Canada"
with open('semanticB.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(headers2)
    for root, dirs, files in os.walk('C:\\Users\\rocki\\PycharmProjects\\csv\\Semantic'):
        if files:
            for filename in files:
                CWordCount = 0
                with open(os.path.join('C:\\Users\\rocki\PycharmProjects\csv\Semantic',filename),'r') as f:
                    contents = f.read()
                    wordcount = len(contents.split())
                for m in pattern.finditer(contents):
                    if m.group()==words[0]:
                        CWordCount += 1
                if CWordCount:
                     csv_writer.writerow([filename, wordcount, CWordCount])
                     # print(filename, CWordCount)
        else:
            print("Empty Directory")


# This will find the article that has highest relative frequency
with open('semanticB.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
      freq = int(row[2])/int(row[1])
      if freq > max:
          max = freq
          articleName = row[0]
    print(articleName,max)
