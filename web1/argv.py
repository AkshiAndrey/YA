import sys


if '--sort' in sys.argv:
    list_ = sys.argv[1:]
    list_.pop(list_.index('--sort'))
    for i, value in enumerate(list_):
        list_[i] = value.split('=')
    list_.sort(key=lambda x: x[0])
else:
    list_ = sys.argv[1:]
    for i, value in enumerate(list_):
        list_[i] = value.split('=')

for i in list_:
    print(f'Key: {i[0]} Value: {i[1]}')
