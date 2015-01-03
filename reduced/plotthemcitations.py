import csv
import matplotlib.pyplot as plt


csvread = csv.reader(open('final_author_percitation_bk.csv','r'))
csvread2 = csv.reader(open('final_author_degreecent.csv','r'))

coauthlist ={}
countcoauthlist ={}
totalcitationlist ={}
avgcitationlist ={}
papercitationlist ={}
eigenlist ={}

for row in csvread:
	countcoauthlist[int(row[0])] = int(row[1])
	coauthlist[int(row[0])] = int(row[2])
	papercitationlist[int(row[0])] = int(row[3])
	totalcitationlist[int(row[0])] = int(row[4])
	avgcitationlist[int(row[0])] = float(row[5])

for row in csvread2:
	eigenlist[int(row[0])] = float(row[1])

# cit = list(citationlist.values())

# cit.sort()
# print(len(cit))
# # print (cit[0])
# # print (cit[1])
# cit = list(set(cit))
# print(len(cit))
# # exit()
# break1 = cit[500]
# break2 = cit[1000]
# break3 = cit[1500]
# break4 = cit[2000]
# break5 = cit[2500]
# break6 = cit[3500]
# print (len(cit))
# print (break1)
# print (break2)
# print (break3)
# print (break4)
# print (break5)
list1 = []
list2 = []
list3 = []
list4 = []
# list5 = []
# list6 = []
# list7 = []
# for key in citationlist:
# 	if citationlist[key] <= break1:
# 		list1.append(coauthlist[key])
# 	elif citationlist[key] <= break2:
# 		list2.append(coauthlist[key])	
# 	elif citationlist[key] <= break3:
# 		list3.append(coauthlist[key])	
# 	elif citationlist[key] <= break4:
# 		list4.append(coauthlist[key])	
# 	elif citationlist[key] <= break5:
# 		list5.append(coauthlist[key])	
# 	elif citationlist[key] <= break6:
# 		list6.append(coauthlist[key])	
# 	else:
# 		list7.append(coauthlist[key])	

# plt.plot(list1,'o')
# plt.plot(list2,'ro')
# plt.plot(list3,'y.')
# plt.plot(list4,'g.')
# plt.plot(list5,'r.')
# plt.plot(list6,'k.')
# plt.plot(list7,'b.')
count= 0
killed = 0
for key in totalcitationlist:
	if key in eigenlist.keys() and avgcitationlist[key]<40 and avgcitationlist[key]>0:
		# if papercitationlist[key] > avgcitationlist[key]:
			# list3.append(avgcitationlist[key])
		# else:
			# list3.append(papercitationlist[key])

		list3.append(countcoauthlist[key])
	# list2.append(totalcitationlist[key])
		# list3.append(avgcitationlist[key])
	# list4.append(countcoauthlist[key])
		list4.append(eigenlist[key])
	else:
		killed+=1
	if(avgcitationlist[key] >=40):
		count+=1
	if(avgcitationlist[key] <= 0):
		count+=1
print(killed)
print(count)
# plt.hist(list4,range=(0.0,0.5))
plt.plot(list4,list3,'b.')
plt.show()