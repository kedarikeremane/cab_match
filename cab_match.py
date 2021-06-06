import sys
import string
import collections
import _decimal
import importlib
import numbers

def avg_drrating(rides,trides,riders,c_ppl):
    i=0
    avg_rating={}
    list1=list(riders.keys())
    while i<len(list1):
        t_value=0
        count=0
        for key, value in riders.items():
            if key == list1[i]:
                t_value+=riders[list1[i]]
        avg_val=t_value/c_ppl[list1[i]]
        av_temp={list1[i]:avg_val}
        avg_rating.update(av_temp)
        i=i+1
    return avg_rating 

def cab_match(avg_r, avg_d, d_name):
    avg_rate=avg_r[d_name]
    list2=list(avg_d.keys())
    list3=list(avg_d.values())
    avg_greater={}
    i=0
    counter1=0
    while i<len(list2):
        if list3[i]>avg_rate:
            avg_greater[list2[i]]=list3[i]
            counter1+=1
        i+=1
    if counter1>0:
        return max(avg_greater, key=avg_greater.get)
    return max(avg_d, key=avg_d.get)
    

i=1
rides={}
riders = {}
drivers = {}
c_ppl={}
while (True):
    rname, rrating, dname, drating=input("Enter rider Name: "), int(input("Enter rider rating given by driver: ")), input("Enter driver name: "), int(input("Enter driver rating given by rider: "))
    rides[i]={rname:rrating, dname:drating}
    if rname not in riders:
        riders[rname]=0
        c_ppl[rname]=0
    riders[rname]=riders[rname]+rrating
    c_ppl[rname]+=1
    if dname not in drivers:
        drivers[dname]=0
        c_ppl[dname]=0
    drivers[dname]+=drating
    print(drivers)
    c_ppl[dname]+=1
    print(c_ppl)
    inp=input("Do you wnt to add one mire ride? Y/N: ")
    if inp.upper()=='N':
        break
    i=i+1
print(rides)
print(drivers)
total_rides=i
avg_rating_riders={}
avg_rating_drivers={}
avg_rating_riders=avg_drrating(rides,total_rides,riders,c_ppl)
avg_rating_drivers=avg_drrating(rides,total_rides,drivers,c_ppl)
print(avg_rating_riders)
print(avg_rating_drivers)
rider_name=input("Enter name of the rider to match that is in the list:")
drive_name=cab_match(avg_rating_riders, avg_rating_drivers, rider_name)
print("The driver that is best match for "+rider_name+" is: "+drive_name)
