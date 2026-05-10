# model.py
import torch.nn as nn

class MagnitudeRegressor(nn.Module):
    def __init__(self, input_dim=16):
        super().__init__()
        self.layer1 = nn.Linear(input_dim, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 16)
        self.layer4 = nn.Linear(16, 1)
        self.silu = nn.LeakyReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.silu(self.layer1(x))
        x = self.dropout(x)
        x = self.silu(self.layer2(x))
        x = self.dropout(x)
        x = self.silu(self.layer3(x))
        x = self.layer4(x)
        return x.squeeze(-1)