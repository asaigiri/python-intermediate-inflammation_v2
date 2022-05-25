import numpy as np
def attach_names(data, names):
    assert len(data)==len(names)
    dict_1 = []
    for name, data in zip(names, data):
        dict_1.append({'name': name, 'data': data})
    return dict_1

data = ([[1., 2., 3.],
                 [4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob'])
print(output)