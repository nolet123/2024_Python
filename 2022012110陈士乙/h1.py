import random


def data_sample_inner(**kwargs):
    result = []
    for k, v in kwargs.items():
        if k == 'int':
            for kk, vv in v.items():
                if kk == 'datarange':
                    range_l = vv[0]
                    range_r = vv[1]
            result.append(random.randint(range_l, range_r))
        elif k == 'float':
            for kk, vv in v.items():
                if kk == 'datarange':
                    range_l = vv[0]
                    range_r = vv[1]
            result.append(random.uniform(range_l, range_r))
        elif k == 'str':
            for kk, vv in v.items():
                if kk == 'datarange':
                    chars = vv
                elif kk == 'len':
                    str_len = vv
            result.append(''.join(random.choice(chars) for _ in range(str_len)))
        elif k == 'tuple':
            tmp = data_sample_inner(**v)
            result.append(tuple(tmp))
        elif k == 'list':
            tmp = data_sample_inner(**v)
            result.append(tmp)
        elif k == 'set':
            tmp = data_sample_inner(**v)
            result.append(set(tmp))
    return result


def data_sample(**kwargs):
    global num
    dc = dict()
    for k, v in kwargs.items():
        if k == 'num':
            num = v
        else:
            dc[k] = v
    result = []
    for _ in range(int(num)):
        result.append(data_sample_inner(**dc))
    return result


if __name__ == '__main__':
    print(data_sample(**{'num': 5, 'tuple': {'int': {'datarange': [1, 10]},
                                             'list': {'int': {'datarange': [1, 10]},
                                                      'float': {'datarange': [1, 10]},
                                                      'str': {'datarange': 'q1w2e3', 'len': 8},
                                                      'tuple': {'str': {'datarange': 'q1w2e3r4t5y6', 'len': 5}}}}}))
