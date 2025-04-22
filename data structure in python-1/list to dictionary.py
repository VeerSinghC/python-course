def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result
students = [[1, 'John doe']]