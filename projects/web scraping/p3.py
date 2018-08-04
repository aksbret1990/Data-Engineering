import requests
from bs4 import BeautifulSoup

def func():
    result = [] #list that will be returned
    response = requests.get("http://www.dot.ca.gov/mail.htm") #request to get the webpage
    soup = BeautifulSoup(response.text,"html.parser") #using Beautiful Soup to parse the respoonse text
    rows = soup.find_all("tr") #finding all table rows

    for i in range(1,len(rows)-1): # we have to iterate from 1st table row because 0th row is header and we excelude last row since
        #it is irrelevant
            mega_elements = rows[i].find_all("td") #we find all the table data
            newdict = {} #craeting an empty dictionary so that we can add respective office information
            for j in range(0,2): #iterate from office data to mailing data
                if j == 0: #iterating over office data
                    xaxa = mega_elements[j].get_text() #get office data
                    xaxalist = xaxa.splitlines() #get a list of this data by splitting on lines
                    for line in range(0,len(xaxalist)):
                        xaxalist[line] = xaxalist[line].replace('\xa0',' ') # replace \xa0 chracter with space
                    xaxalist = [x.strip(' ') for x in xaxalist] #strip the extra space
                    if len(xaxalist) == 5: #some information for names of offices comes on new line so we combine the two lines
                        xaxalist[0:2] = [' '.join(xaxalist[0:2])]     
                    newdict["office_name"] = xaxalist[0] #get office name
                    if xaxalist[0] == "Headquarters":
                        newdict["office_link"] = "http://www.dot.ca.gov/" #get the link if headquarter
                    else:
                        name_list = xaxalist[0].split()
                        number = name_list[1]
                        newdict["office_link"] = "http://www.dot.ca.gov/dist" + number + '/' #get the link if not headquarter
                        
                    newdict["office_address"] = xaxalist[1]  #get office address
                    
                    if ',' not in str(xaxalist[2]): #case when state not present
                         newdict["office_city"] = xaxalist[2]
                         newdict["office_state"] = None
                         newdict["office_zip"] = None
                         newdict["office_phone"] = xaxalist[3]
                        
                    else: #case when state is present
                          city_state_zip = xaxalist[2].split(',')
                          newdict["office_city"] = xaxalist[2].split(',')[0]
                          newdict["office_state"] = xaxalist[2].split(',')[1].split()[0]
                          newdict["office_zip"] = xaxalist[2].split(',')[1].split()[1]
                          newdict["office_phone"] = xaxalist[3]
                
                else: #iterate over mailing address data
                    xaxa = mega_elements[j].get_text()
                    xaxalist = xaxa.splitlines()
                    for line in range(0,len(xaxalist)):
                        xaxalist[line] = xaxalist[line].replace('\xa0',' ')
                    xaxalist = [x.strip(' ') for x in xaxalist]
                    if len(xaxalist) == 2: #case when there are only 2 lines in the data
                        if 'Box' not in xaxalist[0].split(): #case when PO BOX is not there
                            newdict["mail_address"] = xaxalist[0]
                            newdict["mail_pobox"] = None
                            newdict["mail_city"] = xaxalist[1].split(',')[0]
                            newdict["mail_state"] = xaxalist[1].split(',')[1].split()[0]
                            newdict["mail_zip"] = xaxalist[1].split(',')[1].split()[1]
                            newdict["mail_phone"] = None       
                            
                        else: #case when PO Box is there
                            newdict["mail_address"] = None
                            newdict["mail_pobox"] = xaxalist[0]
                            newdict["mail_city"] = xaxalist[1].split(',')[0]
                            newdict["mail_state"] = xaxalist[1].split(',')[1].split()[0]
                            newdict["mail_zip"] = xaxalist[1].split(',')[1].split()[1]
                            newdict["mail_phone"] = None
                            
                    else: #case when there are more than 2 lines in the data
                        newdict["mail_address"] = xaxalist[0]
                        if 'Box' not in xaxalist[1].split():
                            newdict["mail_pobox"] = None
                            newdict["mail_city"] = xaxalist[1].split(',')[0]
                            newdict["mail_state"] = xaxalist[1].split(',')[1].split()[0]
                            newdict["mail_zip"] = xaxalist[1].split(',')[1].split()[1]
                            if len(xaxalist) > 2:
                                newdict["mail_phone"] = xaxalist[2]
                            else:
                                newdict["mail_phone"] = None
                        else:
                            newdict["mail_pobox"] = xaxalist[1]

                            newdict["mail_city"] = xaxalist[2].split(',')[0]
                            newdict["mail_state"] = xaxalist[2].split(',')[1].split()[0]
                            newdict["mail_zip"] = xaxalist[2].split(',')[1].split()[1]                        
                            if len(xaxalist) > 3:
                                newdict["mail_phone"] = xaxalist[3]
                            else:
                                newdict["mail_phone"] = None
            result.append(newdict) #appned the dictionary to the result
    return result
        
        
mli = func()
for i in mli:
    print(i)
    print('\n\n')
