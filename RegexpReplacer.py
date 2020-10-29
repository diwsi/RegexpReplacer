import os
import re

#File pattern to search eg: .cs
filePattern = re.compile('(.*cs$)')
#Search content expression eg:[Column("...")]
searchPattern = r'\[Column\(\".*\]$' 
#Content to replace with eg:""
replacePattern = r'' 
#Path to operate
targetPath = r"D:\\myFolder\\"
#File encoder
encoder="utf8"
for root, dirs, files in os.walk(targetPath):
    for file in files:
        if filePattern.match(file):
            filePath = os.path.join(root, file)
            with open(filePath, 'r', encoding=encoder) as f:
                fileContent = f.read()
            with open(filePath, 'w', encoding=encoder) as f:
                fileContentAltered = re.sub(
                    searchPattern, replacePattern, fileContent, flags=re.M)
                f.write(fileContentAltered)
                f.close()
                print(fileContentAltered)
            print(filePath)
