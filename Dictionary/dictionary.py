#==================================================
#
#   Dictionnary generate.
#
#==================================================

def dictionary(key, value):
    d = {}
    for i in range(0, len(key)):
        if i < len(value):
            d[key[i]] = value[i]
        else:
            d[key[i]] = None
    return d