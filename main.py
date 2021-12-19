def rfile(dir):
    with open(dir, 'r', encoding='utf-8') as f:
        data = list(map(int, f.readline().split()))
    return data


def summa(data):
    sm = 0
    for i in data:
        sm += i
    return sm


def composition(data):
    comp = 1
    for i in data:
        comp *= i
    return comp


def mn(data):
    mn = float('+inf')
    for i in data:
        if i < mn:
            mn = i
    return mn


def mx(data):
    mx = float('-inf')
    for i in data:
        if i > mx:
            mx = i
    return mx


if __name__ == '__main__':
    dt = rfile('file')
    print('Минимальное:', mn(dt), '\nМаксимальное:', mx(dt), '\nСумма:', summa(dt), '\nПроизведение:', composition(dt))
    for i in rfile('file'):
        print(type(i) == int)
