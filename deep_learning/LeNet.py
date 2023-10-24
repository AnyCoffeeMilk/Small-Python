import torch
from torch import nn
import torch.utils.data as Data
from torchvision import transforms
import torchvision.datasets as datasets

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 6, 5),
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2)
        )
        self.fc = nn.Sequential(
            nn.Linear(16*4*4, 120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        feature = self.conv(x)
        output = self.fc(feature.view(x.shape[0], -1))
        return output
    
def eval(net, test_iter):
    acc_sum, n = 0.0, 0
    for x, y in test_iter:
        acc_sum += (net(x).argmax(dim=1) == y).float().sum()
        n += y.shape[0]
    
    return acc_sum / n

num_outputs = 10
num_eqoches = 2
batch_size = 128

train_data = datasets.MNIST(root="./mnist", train=True, download=True, transform=transforms.ToTensor())
train_iter = Data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_data = datasets.MNIST(root="./mnist", train=False, download=True, transform=transforms.ToTensor())
test_iter = Data.DataLoader(train_data, batch_size=batch_size, shuffle=False)

net = LeNet()
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

for epoch in range(num_eqoches):
    for x, y in train_iter:
        y_hat = net(x)
        l = loss(y_hat, y).sum()

        optimizer.zero_grad()
        l.backward()
        optimizer.step()

    print(eval(net, test_iter))
torch.save(net, "C:/Users/ACER/Desktop/Python/DeepLearning/output/softmax_mnist.pt")