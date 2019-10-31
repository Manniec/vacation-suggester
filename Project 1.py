# Project 1
import math


def deg2rad(deg):
    x = (deg * (math.pi / 180))
    return x


def distance(rad1, rad2):
    d = 2.0 * 6360.0 * math.asin(math.sqrt(((math.sin(((rad1 - 0.6522)/2.0)))**2) + (math.cos(0.6522) * math.cos(rad1) * ((math.sin(((rad2 - 2.1066)/2.0)))**2))))
    return d


def geo2dec(d, m):
    g = d + m/60
    return g

#import Formula

cities = open('cities.txt', 'r', encoding="utf-8")
next(cities) #skips first line

# write a new file
# chart first
# append to new list
# N = 1 , S = -1

List = []

for line in cities:
    data = line.strip().split('\t') #sets data var to [latitude, longitude, city, province/state, Country]
    data[0] = data[0].split('°') #splits line to list of [degrees, minutes] -> ['82', '30N'] and saves it to data[0] 
    #data[0][1].endswith('N') #gives you a boolean depending on if N 
    data[0][0] = int(data[0][0]) if data[0][1].endswith('N') else -int(data[0][0]) #converts data[0][0] into int (negative if South, positive if north) 
    """ Above line is equivalent to: 
    if data[0][1].endswith('N'):
        data[0][0]= int(data[0][0]) # where data[0][0] is degrees of latitude and data[0][1] is minutes
    else: 
        data[0][0]= -int(data[0][0])
        
        """
    #[82, '30N']
    data[0][1] = int(data[0][1][:-1]) #removes N or S at end of minutes -> data[0] is now [82, 30]
    data[1] = data[1].split('°')
    data[1][0] = int(data[1][0]) if data[1][1].endswith('W') else -int(data[1][0]) #converts data[0][0] into int (negative if E, because merced is west)
    data[1][1] = int(data[1][1][:-1]) #removes E or W
    List.append(data)
cities.close()

##Taking User Input##
season = input('When would you like to travel? [Summer or Winter]? ') 
climate = input('Would you like to go somewhere [Cold or Warm]? ')

##Case sensitivity##
"""
season = "Summer" =/= "SUmmer" =/= "summer"
season = season.upper() 
"""

##Filter List based on user input##
if season == 'Summer':
    if climate == 'Cold':
        List = list(filter(lambda data: data[0][0] > 66 or data[0][0] <= -35, List))
        """Above code (kinda) same as (how to use lambda):
        def UNNAMED(dataparam):
            if (dataparam[0][0] > 66 or dataparam[0][0] <= -35): # where data[0][0] is degrees of latitude
                return dataparam

        ListNew = [] #empty list
        for data in List:
            ListNew.append(UNNAMED(data))
        

            

        _______________ALTERNATE__________________
        ListNew = []
        for data in List:
            if (data[0][0] > 66 or data[0][0] <= -35): # where data[0][0] is degrees of latitude
                ListNew.append(data)
        List = ListNew
        """
    elif climate == 'Warm':
        List = list(filter(lambda data: data[0][0] <= 66 and data[0][0] > -35, List))

elif season == 'Winter':
    if climate == 'Cold':
        List = list(filter(lambda data: data[0][0] > 35 or data[0][0] <= -66, List))
    elif climate == 'Warm':
        List = list(filter(lambda data: data[0][0] <= 35 and data[0][0] > -66, List))

""" Alternate solution
ListNew = []
if season == 'Summer':
    if climate == 'Cold':
        for data in List:
            if (data[0][0] > 66 or data[0][0] <= -35): # where data[0][0] is degrees of latitude
                ListNew.append(data)
    elif climate == 'Warm':
        #for loop and if data[0][0] <= 66 and data[0][0] > -35

elif season == 'Winter':
    if climate == 'Cold':
        #for loop and if data[0][0] > 35 or data[0][0] <= -66
    elif climate == 'Warm':
        #for loop and if data[0][0] <= 35 and data[0][0] > -66

List = ListNew #set new list equal to List (removes old list, left with only data that matches conditions)

--------------------------------------------------------------
"""




##Calculating Distances##
for data in List: #iterate through List (again data= each row in format -> [[68, 21], [133, 43], 'Inuvik', 'Northwest Territories', 'Canada'])
    latitude = geo2dec(float(data[0][0]), float(data[0][1])) #convert ints to FLOATS & convert to dec
    # remember each element of data looks like -> [[degrees, min], [degrees, min], 'city', 'province/state', 'country']
    latitude = deg2rad(latitude) #convert dec to radians
    longitude = geo2dec(float(data[1][0]), float(data[1][1]))
    longitude = deg2rad(longitude)
    #---------now latitude and longitude are floats (numbers with decimals) and in radians --------------
    #data.append([latitude,longitude])
    #print(data)
    data.append(distance(latitude,longitude)) # take distance & append to data -> [[76, 25], [82, 54], 'Grise Fiord', 'Nunavut', 'Canada', 4716.023691816886]

    #[[DEG, MIN], [DEG,MIN], 'CITY' ,  'STATE/PROV', DIST]#
    #[data[0],     data[1] , data[2], ]
    


##Getting top 5##
List.sort(key=lambda data: data[5]) #sort list by data[5](distance) first longest last
#sort function -> sort(key = )

    

##Print Top 5 Results##
for i in range(5): #range(5) gives iteratible length 5 [0, 1, 2, 3, 4]
    #print( 'Option', i+1, ': ', _____)
    print(List[i])
    

