import os
import shutil

root = '/group/40067/druryxu/SemFew/cifar100/'
with open('/group/40067/druryxu/SemFew/cifar100/splits/bertinetto/val.txt') as f:
    for line in f.readlines():
        shutil.move(os.path.join(root, 'train', line.strip()), os.path.join(root, 'val'))
