def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    dgt=0
    ltr=0
    
    
    for idx in range(len(txt)):
        if txt[idx].isdigit():
            dgt+=1
        if txt[idx].isalpha():
                ltr+=1
    dict={'Letters':ltr,'Digits':dgt}
    
    return dict
print(count_all('This car costs 95400 usd'))