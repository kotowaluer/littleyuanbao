from UNet.model import UNet

model = UNet()
for n in model.modules():
    print(n)
