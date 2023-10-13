import torch
import torch.utils.data as Data
from torchvision import transforms
import torchvision.datasets as datasets

import cv2

train_data =  datasets.MNIST(root="./mnist", train=True, download=True, transform=transforms.ToTensor())
train_iter = Data.DataLoader(train_data, batch_size=10, shuffle=True)

test_data = datasets.MNIST(root="./mnist", train=False, download=True, transform=transforms.ToTensor())
test_iter = Data.DataLoader(train_data, batch_size=10, shuffle=True)

for x, y in train_iter:
    print(x.shape)
    print(y.shape)
    cv2.imshow("", x[0].view(28,28).numpy())
    cv2.waitKey