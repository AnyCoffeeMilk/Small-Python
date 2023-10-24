import torch
from torch import nn
import torch.optim as optim
from torch.autograd import Variable
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(561, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, 6)
        )
        
    def forward(self, x):
        y = self.net(x)
        return y

epochs = 100
batch_size = 64
lr = 0.001

df_train = pd.read_csv("C:/Users/ACER/Desktop/Python/DeepLearning/input/humanActivity/train.csv")
df_test = pd.read_csv("C:/Users/ACER/Desktop/Python/DeepLearning/input/humanActivity/test.csv")

df_train.drop(['subject'], axis = 1, inplace = True)
df_test.drop(['subject'], axis = 1, inplace = True)

train = df_train.copy()
test = df_test.copy()

train['Activity'] = train['Activity'].astype('category').cat.codes
test['Activity'] = test['Activity'].astype('category').cat.codes

x = train.drop(['Activity'], axis = 1).values
y = train['Activity'].values
y = y.reshape(y.shape[0], 1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

X_train = torch.from_numpy(X_train).type(torch.FloatTensor)
X_test = torch.from_numpy(X_test).type(torch.FloatTensor)
y_train = torch.from_numpy(y_train).type(torch.FloatTensor)
y_test = torch.from_numpy(y_test).type(torch.FloatTensor)

net = Net()
loss = nn.CrossEntropyLoss()
opt = torch.optim.SGD(net.parameters(), lr=lr)
accuracy = 0

for epoch in range(epochs):
    for i in range(0, X_train.size(0), batch_size):
        x_batch = X_train[i:i + batch_size, :]
        y_batch = y_train[i:i + batch_size, :]
        x_batch = torch.tensor(x_batch)
        y_batch = torch.tensor(y_batch, dtype = torch.long)
        y_batch = y_batch.view(y_batch.shape[0])

        y_hat = net(x_batch)

        l = loss(y_hat, y_batch).sum()

        opt.zero_grad()
        l.backward()
        opt.step()

    net.eval()
    y_pred = torch.argmax(net(X_test), dim=1)
    ac = accuracy_score(y_test, y_pred)
    net.train()

    if accuracy < ac:
        accuracy = ac
        torch.save(net, "C:/Users/ACER/Desktop/Python/DeepLearning/output/best_net.pt")

model = torch.load("C:/Users/ACER/Desktop/Python/DeepLearning/output/best_net.pt")
model.eval()

t = test.drop(['Activity'], axis = 1).values
t = torch.from_numpy(t).type(torch.FloatTensor)

y_t = test['Activity'].values
y_net = torch.argmax(net(t), dim=1)

print(accuracy_score(y_t, y_net))