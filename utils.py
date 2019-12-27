def find_max(list):
    _max = 0
    for num in list:
        if int(num) > _max:
            _max = int(num)
    
    return _max