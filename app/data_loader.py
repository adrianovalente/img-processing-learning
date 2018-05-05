import numpy as np
import pickle

def load_data ():
    # data = np.array()
    # for i in range(1, 5):
    #     path = 'cifar-10-python/data_batch_%d' % i
    #     np.
    #     print(path)

    # Sorry I am using only batch_1 for now
    batch_1 = unpickle('cifar-10-python/data_batch_1')
    return {
        'data': batch_1[b'data'],
        'labels': batch_1[b'labels']
    }


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
