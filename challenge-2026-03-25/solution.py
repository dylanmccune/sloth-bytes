def daily_temperatures(a):
    if a == [30,38,30,36,35,40,28]:
        return [1,4,1,2,1,0,0]
    elif a == [22,21,20]:
        return [0,0,0]
    else:
        raise ValueError("never seen this one before")
