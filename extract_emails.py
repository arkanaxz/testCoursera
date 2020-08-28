import re
import pandas as pd

def save_list(L, filename):
    file = open(filename, 'w')
    for item in L:
        file.write("{} \n".format(item))
    file.close()

#load excel file
file = 'Internet-of-Things_IoT_Survey_June19_7.xlsx'
df = pd.read_excel(file)

#reg ex
validation = re.compile(r'^.+@.+')

#iterate through all cells and collect email addresses
email_adds = []
for col in df.columns:
    for i in range(df.shape[0]):
        element = df[col][i]
        #..check if string, else skip
        if not isinstance(element, str):
            continue
        if validation.match(element):
            email_adds.append(element)
        
#save list of addresses to txt file
filename = 'emails.txt'
save_list(email_adds, filename)