import torch
from torch import nn
import torch.utils.data as Data
from torchvision import transforms
import torchvision.datasets as datasets

from PIL import Image

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

preprocess = transforms.Compose([
    transforms.Resize(28),
    transforms.ToTensor(),
])

models = torch.load("C:/Users/ACER/Desktop/Python/DeepLearning/output/softmax_mnist.pt")
models.eval()

img = Image.open("C:/Users/ACER/Desktop/Python/DeepLearning/input/test.png").convert("L")
img = preprocess(img).unsqueeze(dim=0)

out = models(img)
val, idx = torch.topk(out, 1)
print("-------------\nIt is " + str(idx[0].item()) + "\n-------------")