def all_thing_is_obj(object: any) -> int:
    type_class = type(object)
    tt = ""
    if type_class == str:
        tt = f"{object} is in the kitchen"
    elif type_class == list:
        tt = "List"
    elif type_class == tuple:
        tt = "Tuple"
    elif type_class == set:
        tt = "Set"
    elif type_class == dict:
        tt = "Dict"
    else :
        print("Type not found") ; return 42

    
    print(f"{tt} : {type(object)}")

    return 42


