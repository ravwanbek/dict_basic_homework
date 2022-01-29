from operator import le
import re


def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    a=[]
    for x in people.values():
        a.append(x)
    
    largest=a[0]

    for y in a:
            if y>largest:
                largest=y
    for i,j in people.items():
        if j==largest:
            return str(i)





        



print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))