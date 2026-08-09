def NULL_not_found(object: any) -> int:
    if object is None:
        heading = "Nothing"
    elif type(object) == float and object != object:
        heading = "Cheese"
    elif type(object) == int and object == 0:
        heading = "Zero"
    elif type(object) == str and object == "":
        heading = "Empty"
    elif type(object) == bool and object == False:
        heading ="Fake"
    else:
        print("Type not Found")
        return 1
    
    print(heading, ": ", object, " ", type(object))
    return 0



