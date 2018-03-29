listre = [{'name': 'govnoed'}, {'name': 'andrey'}, {'name': 'sergey'}, {'name': 'hodor'}]

print(listre[-1])


def namelist(names):
    a = []
    for x in names:
        a.append(x['name'])
    if len(a) <= 2:
        return ' & '.join(a[len(a) - 2:])
    else:
        return ', '.join(a[0:len(a) - 2]) + ', ' + ' & '.join(a[len(a) - 2:])


def namelist1(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


print(namelist1(listre))
