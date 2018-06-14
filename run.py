
a = []
l1 = ['normal', 'cpu', 'mem', 'io']
for i in ('bono', 'homestead', 'sprout'):
    for j in l1:
        a.append('%s_%s' % (i, j))

print a
