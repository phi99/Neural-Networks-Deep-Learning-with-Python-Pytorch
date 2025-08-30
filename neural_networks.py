#in progress
import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
  def __init__(self, in_features=4, h1=5, h2=7, out_features=2):
    super().__init__()
    self.layer1=nn.Linear(in_features, h1)
    self.layer2=nn.Linear(h1,h2)
    self.out=nn.Linear(h2, out_features)

  def forward(self,x):
    x=F.relu(self.layer1(x))
    x=F.relu(self.layer2(x))
    x=self.out(x)

    return x

torch.manual.seed(41)
model=Model()
