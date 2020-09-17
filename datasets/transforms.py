from torchvision import transforms


def build_transform():
    transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])])
    return transform
