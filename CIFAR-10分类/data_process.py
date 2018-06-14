import torchvision as tv
import torchvision.transforms as transforms
from torchvision.transforms import ToPILImage
import torch as t
show = ToPILImage() #Could convert Tensor to Image, to visualize
transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

trainset = tv.datasets.CIFAR10(
    root = 'G:/CIFAR10/',
    train= True,
    download=True,
    transform=transforms,
)
train_loader = t.utils.data.Dataloader(
    trainset,
    batch_size=4,
    shuffle=True,
    numworkers=0)

testset = tv.datasets.CIFAR10(
    'G:/CIFAR10/',
    train=False,
    download=True,
    transform = transforms
)

test_loader = t.utils.data.Dataloader(
    testset,
    batch_size=4,
    shuffle=True,
    numworkers=0)

classes = ('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')

(data,label)=trainset[100]
print(classes[label])
show((data+1)/2).resize((100,100))

dataiter = iter(train_loader)
images,labels = dataiter.next()
print(' '.join('%11s'%classes[labels[j]] for j in range(4)))
show(tv.utils.make_grid((images+1)/2)).resize((400,100))
