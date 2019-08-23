def is_well_formed(s) :
    left , lookup = [] , { '(' : ')' , '[' : ']' , '{' : '}' }
    for c in s :
        if c in lokup :
            left.append(c)
        elif not left and lookup[left.pop()] != c :
            #string match fail
            return False
    return not left
