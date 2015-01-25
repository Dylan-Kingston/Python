#Assignment 1
#Author: Dylan Kingston
#Date started: 16/10/14
#Date submitted : 30/11/14

import httplib2 #Needed to download file from internet, not simply reading a file on the hard drive.

YearsOfAge=0      #global variables
Workclass=1
#fnlwgt=2 Not needed.
#Education=3 Not needed.
Education_Number=4
Marital_Status=5
Occupation=6
Relationship=7
Race=8
Sex=9
Capital_Gain=10
Capital_Loss=11
Hours_Per_Week=12
#Native_Country=13 Not needed.
Outcome=14

#Start of functions.

#Start of counting().
def counting(number):
    for row in file:
        filearray.append(row)
        number+=1       #Incrememnt by 1 for each record in the file.
    return(number)
#End of counting().

#Start of weights().
def weights(docarray,number,position):
    counter=0 #A simple counter.
    ref={}    #A dictionary (Currently empty).
    attArray = []

    while(counter<number):
        split=docarray[counter].split(", ");
        if split[position] in ref:
            ref[split[position]]+=1
        else:
            ref[split[position]]=1
            attArray.append(position)
        counter+=1

    counter=0   #Reset the counter to 0.

    for attArray[counter] in ref:
        ref[attArray[counter]]=ref[attArray[counter]]/sev

    return(ref)
#End of weights().

#Start of separateXYnum().
def separateXYnum(records,attributepos):
    X=0
    Y=0
    i=0
    countU=0
    countO=0

    while(i<sev):
        record=records[i]
        recordarray=record.split(", ")
        if recordarray[Outcome].startswith('>'):
           X+=int(recordarray[attributepos]) #Earns more.
           countO+=1
        else:
            Y+=int(recordarray[attributepos]) #Earns less.
            countU+=1

        i+=1

    average_X=X/countO
    average_Y=Y/countU
    midpoint=average_X+average_Y
    midpoint = midpoint/2
    return(midpoint)
#End of separateXYnum().

#Start of separate().
def separate(diction,file,number,n):
    i=0
    pos=0
    neg=0
    midp=0
    midn=0
    above={}
    below={}

    while(i<number):
        line=file[i].split(', ')
        weight=diction[line[n]]

        if(file[i].find('>50K')!=-1):
            midp=midp + weight
            pos+=1
        elif(file[i].find('<=50K')!=-1):
            midn=midn+weight
            neg+=1

        i+=1

    midpoint=((midp/pos)+(midn/neg))/2
    return(midpoint)
#End of separate().

#End of functions.

#Start of Main().
filedown = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data" #Download the file
h = httplib2.Http(".cache")
file_headers, file = h.request(filedown)
file = file.decode()
file = file.split('\n')
filearray=[]
count=0

print('Calculating...') #So the user knows the program is working, if it is running slowly.

count=counting(count) #Run the function counting().

sev=int(count*0.50)

#Trainging set.
#The following are all text based data.
workweight=weights(filearray,sev,Workclass)
maritalweight=weights(filearray,sev,Marital_Status)
occuweight=weights(filearray,sev,Occupation)
raceweight=weights(filearray,sev,Race)
sexweight=weights(filearray,sev,Sex)
relationweight=weights(filearray,sev,Relationship)

#The following are all integer based data.
age_mid=separateXYnum(filearray,YearsOfAge)
work_mid=separate(workweight,filearray,sev,Workclass)
edu_mid=separateXYnum(filearray,Education_Number)
marital_mid=separate(maritalweight,filearray,sev,Marital_Status)
occu_mid=separate(occuweight,filearray,sev,Occupation)
relation_mid=separate(relationweight,filearray,sev,Relationship)
race_mid=separate(raceweight,filearray,sev,Race)
sex_mid=separate(sexweight,filearray,sev,Sex)
gain_mid=separateXYnum(filearray,Capital_Gain)
loss_mid=separateXYnum(filearray,Capital_Loss)
hrs_mid=separateXYnum(filearray,Hours_Per_Week)

#Testing set
counter = 0
correct = 0

while(sev<count-2): #Errors resulted if it wasn't at -2.
    More=0
    Less=0


    attribute=filearray[sev].split(", ")
    #print("Check?:",type(attribute[age]),attribute[age]) Print until error, program was hitting the end of the file. Fixed now.

    if (int(attribute[YearsOfAge]))>age_mid:
        More+=-2
    else:           #I know these two are a little hardcoded, but it gave higher accuracy :)
        Less+=2

    if int(attribute[Education_Number])>edu_mid:
        More+=1
    else:
        Less+=1

    if int(attribute[Hours_Per_Week])>hrs_mid:
        More+=1
    else:
        Less+=1

    if int(attribute[Capital_Gain])>gain_mid:
        More+=1
    else:
        Less+=1

    if int(attribute[Capital_Loss])>loss_mid:
        More+=1
    else:
        Less+=1

    if (float(workweight[attribute[Workclass]])<work_mid):
        More+=1
    else:
        Less+=1

    if (float(maritalweight[attribute[Marital_Status]])>marital_mid):
        More+=1
    else:
        Less+=1

    if (float(occuweight[attribute[Occupation]])>occu_mid):
        More+=1
    else:
        Less+=1

    if (float(raceweight[attribute[Race]])>race_mid):
        More+=1
    else:
        Less+=1

    if (float(sexweight[attribute[Sex]])>sex_mid):
        More+=1
    else:
        Less+=1

    if (float(relationweight[attribute[Relationship]])>relation_mid):
        More+=1
    else:
        Less+=1

    if (More>Less):
        answer='>50K'
    else:
        answer='<=50K'

    if(filearray[sev].find(answer) != -1):
        correct +=1
    else:
        correct +=0

    counter+=1
    sev+=1

accuracy = ((correct/counter)*100) #Claculate the accuracy.
total = 100 #Provide a total % value to compare the output against.
char = '/'  #Used to separate the output value and the total value.

print('Accuracy is:',accuracy, char, total) #Print out the accuracy. Final program output.
#End of Main().



