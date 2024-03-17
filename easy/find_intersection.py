def FindIntersection(strArr):
    lists = [x.split(', ') for x in strArr]
    intersection_set = set(lists[0]).intersection(set(lists[1]))
    intersection_list = [x for x in intersection_set]
    intersection_list.sort(key=lambda x: int(x))
    return ','.join(intersection_list)
