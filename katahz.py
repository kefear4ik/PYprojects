listre = [{'name': 'govnoed'}, {'name': 'andrey'}, {'name': 'sergey'}, {'name': 'hodor'}]





def namelist(names):
    a = []
    for x in names:
        a.append(x['name'])
    if len(a) <= 2:
        return ' & '.join(a[len(a) - 2:])
    else:
        return (', '.join(a[0:len(a) - 2]) + ', ' + ' & '.join(a[len(a) - 2:]))



