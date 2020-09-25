"""
A simple traffic light change function that uses assertion example.
Assert is a sanity check.
Also, if assert fails your program SHOULD crash, unlike exceptions.
Assertions are for programmer errors not user errors.
User errors should reaise exeptions.
"""
market_2nd = {'ns':'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red! ' + str(intersection)

switchLights(market_2nd)
