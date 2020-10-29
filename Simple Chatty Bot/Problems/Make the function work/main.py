def closest_higher_mod_5(x):   
    y = x % 5
    
    if y == 0:
        return x
    else:
        z = 5 - y
        return x + z
