def is_odd(number):

    if (number % 2 == 0):
        return False
    else: 
        return True

    # return bool(number%2) 

def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(103) == True
    print("Your code is Correct!")
test_is_odd() 