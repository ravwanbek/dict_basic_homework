def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dict={}
    for x in range(len(key)):
        dict.update({key[x]:value[x]})


    return dict
print(create_dictionary(['Uzbekistan','Kazakhstan','Korea'],['uz','kz','kr']))