import torch
import torch.utils.data as Data
import torch.nn as nn
import torch.optim as optim

class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)
    
    def forward(self, x):
        y = self.linear(x)
        return y

def generate_data(num_inputs, num_examples):
    w = torch.tensor([[10.2],[-19.1]])
    b = torch.tensor(4.8)

    x = torch.randn(num_examples, num_inputs, dtype=torch.float32)
    y = torch.mm(x,w) + b
    y += torch.normal(mean=torch.zeros(num_examples,1), std=0.1 * torch.ones(num_examples, 1))

    return x, y

num_inputs = 2
num_examples = 50000
num_epochs = 5
batch_size = 100

features, labels = generate_data(num_inputs, num_examples)
train_data = Data.TensorDataset(features, labels)
data_iter = Data.DataLoader(train_data, batch_size, shuffle=True)

net = LinearNet(num_inputs)
loss = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.03)

for epochs in range(num_epochs):
    for x, y in data_iter:
        y_hat = net(x)
        l = loss(y_hat, y)

        optimizer.zero_grad()
        l.backward()
        optimizer.step()

        print(l)

for param in net.parameters():
    print(param)