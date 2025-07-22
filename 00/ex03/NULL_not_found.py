def NULL_not_found(object: any) -> list :
    type_class = type(object)
    name = ""

    if object == None :
        name = "Nothing"
    # nan은 결코 그 자체와 같지 않음
    elif type(object) == float and object != object:
        name = "Cheese"
    elif object == 0 and type(object) == int :
        name = "Zero" 
    elif object == "" :
        name = "Empty"
    elif object == False and type(object) == bool :
        name = "Fake"
    else :
        print("type not found"); return 1

    print(f"{name}: {object}{'' if object=='' else ' '}{type(object)}")

    return 0
