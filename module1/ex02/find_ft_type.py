def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            heading = "List"
        case tuple():
            heading = "Tuple"
        case set():
            heading = "Set"
        case dict():
            heading = "Dict"
        case str():
            heading = f"{object} is in the kitchen"
        case _:
            print("Type not found")
            return 42
    print(heading, " : ", type(object))
    return 42
