def str_combine(name1, name2):
    # return name1 + " " + name2
    return f"{name1}{name2}"


family_name = input("Input your family name==>")
first_name = input("Input your first name==>")
print(str_combine(family_name, first_name))
