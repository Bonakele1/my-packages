from mypackages import myModule

def test_top_n ():
    """ make sure top n works correctly
    """ 

    assert myModule.top_n([10,9,8,7,6], 3) == [10,9,8], "Incorrect"
    assert myModule.top_n([7,8,5,9,11], 2) == [11,9], "Incorrect"
    assert myModule.top_n([1,2,3,4,5,6], 5) == [6,5,4,3,2], "Incorrect"