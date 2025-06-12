def my_function(**name):
    print("Surname of the family is " + name["lname"])
    for k, val in name.items():
        print(k, val)

my_function(fname="Kartik", lname="Gamne")