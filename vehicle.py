t = 0 # defining variables for usage in loops
number_new_car = 0

# Creating CLASS
class Vehicles(object):
    def __init__(self, brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

# Creating OBJECTS
ford = Vehicles(brand="Ford", model="Mustang GT 350", km="80250", service_date="03.02.2016")
peugeot = Vehicles(brand="Peugeot", model="307 1.6", km="95000", service_date="07.06.2016")
porsche = Vehicles(brand="Porsche", model="918 Spyder", km="80250", service_date="09.11.2015")
bmw = Vehicles(brand="BMW", model="1er Coupe", km="32000", service_date="03.02.2017")
jeep = Vehicles(brand="Jeep", model="Wrangler", km="12000", service_date="04.03.2017")

brands = [ford, peugeot, porsche, bmw, jeep] # defining "brands"-list for later on

print "**********************************"
print "Vehicle Manager Program v 1.0 beta"
print "**********************************"

q = raw_input("PRESS ==> l <== to view list of company vehicles \nPRESS ==> e <== to change km / service date \nPRESS ==> a <== to add a new vehicle >> " )

if q == "l":
    print ""
    print "LIST OF VEHICLES"
    print "================"
    for counter in brands: # counter counting my "brands"-list from 1st to last item
        print counter.brand + " " + counter.model

if q == "e":

    print""
    print "EDITING KM AND GENERAL SERVICE DATE"
    print "==================================="
    for counter in brands:
        t += 1
        print t , counter.brand + " " + counter.model + ", " + counter.km + " km, last service date: " + counter.service_date

    print ""
    q2 = raw_input("which car to change km/service date? press number 1 - 5 >> ")

    if q2 == "1":
        print "adapting " + "car 1: " + " " + ford.brand + " " + ford.model + ", " + ford.km + " km, last service date: " + ford.service_date
        new_km = raw_input("Enter new km-amount >> ")
        new_date = raw_input("Enter new service-date >> ")
        ford = Vehicles(brand="Ford", model="Mustang GT 350", km=new_km, service_date=new_date)
        print "data changed to: " + ford.brand + " " + ford.model + ", " + ford.km + " km, last service date: " + ford.service_date

    elif q2 == "2":
        print "adapting " + "car 2: " + " " + peugeot.brand + " " + peugeot.model + ", " + peugeot.km + " km, last service date: " + peugeot.service_date
        new_km = raw_input("Enter new km-amount >> ")
        new_date = raw_input("Enter new service-date >> ")
        peugeot = Vehicles(brand="Peugeot", model="307 1.6", km=new_km, service_date=new_date)
        print "data changed to: " + peugeot.brand + " " + peugeot.model + ", " + peugeot.km + " km, last service date: " + peugeot.service_date

    elif q2 == "3":
        print "adapting " + "car 3: " + " " + porsche.brand + " " + porsche.model + ", " + porsche.km + " km, last service date: " + porsche.service_date
        new_km = raw_input("Enter new km-amount >> ")
        new_date = raw_input("Enter new service-date >> ")
        porsche = Vehicles(brand="Porsche", model="918 Spyder", km=new_km, service_date=new_date)
        print "data changed to: " + porsche.brand + " " + porsche.model + ", " + porsche.km + " km, last service date: " + porsche.service_date

    elif q2 == "4":
        print "adapting " + "car 4: " + " " + bmw.brand + " " + bmw.model + ", " + bmw.km + " km, last service date: " + bmw.service_date
        new_km = raw_input("Enter new km-amount >> ")
        new_date = raw_input("Enter new service-date >> ")
        bmw = Vehicles(brand="BMW", model="1er Coupe", km=new_km, service_date=new_date)
        print "data changed to: " + bmw.brand + " " + bmw.model + ", " + bmw.km + " km, last service date: " + bmw.service_date

    elif q2 == "5":
        print "adapting " + "car 5: " + " " + jeep.brand + " " + jeep.model + ", " + jeep.km + " km, last service date: " + jeep.service_date
        new_km = raw_input("Enter new km-amount >> ")
        new_date = raw_input("Enter new service-date >> ")
        jeep = Vehicles(brand="Jeep", model="Wrangler", km=new_km, service_date=new_date)
        print "data changed to: " + jeep.brand + " " + jeep.model + ", " + jeep.km + " km, last service date: " + jeep.service_date



if q == "a":
    number_new_car += 1
    print""
    print "ADDING NEW VEHICLE"
    print "=================="
    brand_new = raw_input("insert  brand >> ")
    model_new = raw_input("insert model >> ")
    km_new = raw_input("insert km >> ")
    service_date_new = raw_input("insert service date >> ")

    new_car = Vehicles(brand = brand_new, model = model_new, km = km_new, service_date = service_date_new) # creating new object new_car
    print "New car added:" , str(5+ number_new_car) + ": " + new_car.brand + " " + new_car.model + ", " + new_car.km + " km, last service date: " + new_car.service_date

print ""
print "DATA FILE CREATED (store_file.txt)"
print "=================================="

store_file = open("store_file.txt", "w+") # creating new text file "store_file.txt"
store_file.write("List of company cars:\n=====================\n")
store_file.write("car 1: " + " " + ford.brand + " " + ford.model + ", " + ford.km + " km, service date: " + ford.service_date + "\n")
store_file.write("car 2: " + " " + peugeot.brand + " " + peugeot.model + ", " + peugeot.km + " km, service date: " + peugeot.service_date + "\n")
store_file.write("car 3: " + " " + porsche.brand + " " + porsche.model + ", " + porsche.km + " km, service date: " + porsche.service_date + "\n")
store_file.write("car 4: " + " " + bmw.brand + " " + bmw.model + ", " + bmw.km + " km, service date: " + bmw.service_date + "\n")
store_file.write("car 5: " + " " + jeep.brand + " " + jeep.model + ", " + jeep.km + " km, service date: " + jeep.service_date + "\n")

if number_new_car != 0: # if new car added ==> printout to file as well
    store_file.write("car " + str(5+ number_new_car) + ":  " + new_car.brand + " " + new_car.model + ", " + new_car.km + " km, service date: " + new_car.service_date + "\n")

print "END"





















