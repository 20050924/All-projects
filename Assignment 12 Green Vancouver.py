#Michael Li
#Computers 10
#2021/6/21
#A program that sort out informations in Green Vancouver project
file = open("green vancouver.txt")
totaldata = []
Local_food_projects = 0
names_of_projects_have_no_URL1_2 = []
areas = []
Bikenames = []
for data in file:
    linelist = data.split(";")
    totaldata.append(linelist)
for lineitem in totaldata:
    if lineitem[3] == "Local-Food" and lineitem[10] == "Downtown\n":
        Local_food_projects += 1
    if lineitem[6] == "" and lineitem[7] == "":
        names_of_projects_have_no_URL1_2.append(lineitem[1])
    if lineitem[10] not in areas:
        areas.append(lineitem[10])
    if "Bike" in lineitem[1] and lineitem[1] not in Bikenames:
        Bikenames.append(lineitem[1])
for i in range(24):
    areas[i] = areas[i].rstrip()
del areas[0]
areas.sort()
del areas[0]
print(f"There are {Local_food_projects} Local-Food projects in Downtown","\n","\n")
print(f"Names of project that doesn't have 1st and 2nd websites are {names_of_projects_have_no_URL1_2}","\n","\n")
print(f"These are areas represented{areas}","\n","\n") #All areas represented
print(f"Project names with Bike in it{Bikenames}")