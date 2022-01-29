def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    
    dict={}
    for x in range(len(cities)):
        
        dict.update({x:cities[x]})



    return dict
print(cities_dict(['tashkent','seoul','busan','tokyo','paris','amsterdam','barcelona','lyon','brussels','munchen','geneva','phuket']))
