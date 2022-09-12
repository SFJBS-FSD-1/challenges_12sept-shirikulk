#Challenge 1:  Write a function that takes a natural number as input and outputs the number of digit in it.
# Conversion of number to string is not allowed

# data = int(input("enter a number: "))
# count = 0
#
# while data != 0:
#     data //=10
#     count +=1
#
# print("number of digits: " + format(count))


#Challenge 2:  Write a function that takes a natural number as input and outputs the reverse of that number.
# Conversion of number to string is not allowed

# number = int(input("enter a number: "))
# revs_number = 0
#
# while (number > 0):
#     rem = number % 10
#     revs_number = (revs_number * 10) + rem
#     number = number // 10
#
# print("the reverse number is : {}".format(revs_number))


#Challenge 3 : Write a function where user will enter a natural number as input and output returns the number of zeroes in the end of the factorial of that number.
# Conversion of number to string is not allowed

# data = int(input("enter a number:"))
# count = 0
# while (data >= 5):
#         data //= 5
#         count += data
#
# print("no of zeroes is" + str(count))


#Challenge 4 : list1 = ["India" , "England", "Spain"]
#list2 = ["Delhi","London","Madrid"]
#dict1 = {“India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}
#Write your own function that takes list1 and list2 as inputs and returns a dictionary like


# list1 = ["India" , "England", "Spain"]
# list2 = ["Delhi","London","Madrid"]
#
# res = {}
# for key in list1:
#     for value in list2:
#         res[key] = value
#         list2.remove(value)
#         break
#
# print ("final dictionary is : " + str(res))


#Challenge 5 :
#Write code to create a new dictionary using given dictionary
#
# city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
#
#              “Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”} }

places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}

new_dict = dict([(value, key) for key, value in places.items()])
print("dict after swapping: " + str(new_dict))



# lat = []
# long = []
# plc = []
# for i in places:
#     lat.append(i[0])
#     long.append(i[1])
#     plc.append(places[i[0], i[1]])
#
# print(lat)
# print(long)
# print(plc)

#Challnege 6 : Given mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
#Using for loop find the sum of all even numbers in mylist


# mylist  =  [3,5,4,6,9,10,2,8,7,1]
# result = 0
# for item in mylist:
#     if not item%2:
#         result += item
#
# print("the sum of even numbers is" + str(result))




