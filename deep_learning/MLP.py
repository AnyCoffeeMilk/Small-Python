import torch
from torch import nn
import torch.utils.data as Data
from torchvision import transforms
import torchvision.datasets as datasets

class MLP(nn.Module):
    def __init__(self, num_inputs, num_hiddens, num_outputs):
        super(MLP, self).__init__()
        self.net = nn.Sequential(nn.Linear(num_inputs, num_hiddens),
                                 nn.ReLU(),
                                 nn.Linear(num_hiddens,num_hiddens),
                                 nn.ReLU(),
                                 nn.Linear(num_hiddens,num_hiddens),
                                 nn.ReLU(),
                                 nn.Linear(num_hiddens,num_outputs))

    def forward(self, x):
        x = x.view(x.shape[0], -1)
        y = self.net(x)

        return y
    
def eval(net, test_iter):
    acc_sum, n = 0.0, 0
    for x, y in test_iter:
        acc_sum += (net(x).argmax(dim=1) == y).float().sum()
        n += y.shape[0]
    
    return acc_sum / n

num_inputs = 28 * 28
num_outputs = 10
num_eqoches = 1
batch_size = 64

train_data = datasets.MNIST(root="./mnist", train=True, download=True, transform=transforms.ToTensor())
train_iter = Data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_data = datasets.MNIST(root="./mnist", train=False, download=True, transform=transforms.ToTensor())
test_iter = Data.DataLoader(train_data, batch_size=batch_size, shuffle=False)

net = MLP(num_inputs, 1024, num_outputs)
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.1)

for epoch in range(num_eqoches):
    for x, y in train_iter:
        y_hat = net(x)
        print(y)
        l = loss(y_hat, y).sum()

        optimizer.zero_grad()
        l.backward()
        optimizer.step()

    print(eval(net, test_iter))