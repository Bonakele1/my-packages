def top_n (items, n):
    """Return top n items in an array, in descending order.

    Args:
        Items (array): list or array-like object
        n (int): number of items to return 
    
    Return : 
        array: top n items in descending order
    """
   
    sort_arr = sorted(items, reverse=True)
    return sort_arr[:n]
