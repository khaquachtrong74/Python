import io
import numpy as np
import torch.onnx
import torch.nn as nn

model_path = "/path/to/model"
state_dict = torch.load(model_path, map_location=torch.device('cpu'))

num_classes = 11
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        )
        self.global_pool = nn.AdaptiveAvgPool2d((1,1))  # Không phụ thuộc size ảnh
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, 512), nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.global_pool(x)
        x = self.classifier(x)
        return x
print(state_dict.keys)
model = SimpleCNN(num_classes)
model.load_state_dict(state_dict)
model.eval

dummy_input = torch.randn(1,3,256,256)
torch.onnx.export(
        model,
        dummy_input,
        "cnn_tomato.onnx",
        input_names=['input'],
        output_names=['output'],
        opset_version=11,
        do_constant_folding=True,
        )
