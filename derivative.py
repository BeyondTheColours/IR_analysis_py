def d_dx(data):
    res = []
    l = len(data)
    if l in [0,1]:
        return res

    count = 0

    while count < l-1:
        p1 = data[count]
        p2 = data[count+1]
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        grad = (y2-y1)/(x2-x1)
        new_point = (x1, grad)
        res.append(new_point)

        count += 1
    return res

