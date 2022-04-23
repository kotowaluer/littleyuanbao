import torch
from torch import nn
from UNet.model import UNet

class Generator(nn.Module):
    def __init__(self, in_channel, out_channel):

