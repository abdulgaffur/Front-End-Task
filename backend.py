a= [] #declaring list
n=int(input("Enter number of leads you need to sort: "))#number of leads 
for  i in range(n):
    #input the leads values using for loop
    a.append(input("Enter the leads "))   
def list(lead_email):
    #recursive function to sort the list with respective company domain
    emails={ } 
    domains={ }
    #Dictionaries for the leadlist
    for l in lead_email:
        domainname=l[l.index('@')+1:l.index('.')]
        #Regular expression to to extract domain name
        leads=l 
        #to store leads
        if(domainname not in emails):
            #check whether domainname matches leads emails 
            emails[domainname]=[ ]
            #create list with domainname
            emails[domainname].append(leads)
            #append the matching emails
            domains[domainname]=1
        else:
            emails[domainname].append(leads)
            domains[domainname]+=1
            #append emails matching with domainname
    return emails, domains            
print(list(a))
#recursive function for displaying the seperated domainname and leads
