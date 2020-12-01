
import sys
print(sys.getdefaultencoding())

import pandas as pd

df = pd.read_csv('rawData.csv')
brand = df['Brand']
logo = df['Logo']
color = df['Color']
coreWords = df['Core Words']
usage = df['Usage']

# print(color)


result=[]


for b in brand:
    if not (str(b).lower() =='nan'):
        for l in logo:
            if not (str(l).lower() =='nan'):
                for cl in color:
                    if not (str(cl).lower() == 'nan'):
                        for c in coreWords:
                            if not (str(c).lower() =='nan'):
                                for u in usage:
                                    if not (str(u).lower() =='nan'):
                                        title = str(b).title() + ' ' + str(l).title() + ' ' + str(cl).title() + ' ' + str(c).title() + str(u).title()
                                        result.append(title)
                                        title = ''

# print(result)
ex = pd.DataFrame(result)
ex.to_csv('export.csv')
