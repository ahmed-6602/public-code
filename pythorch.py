import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Create a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the model
model = SimpleNet()

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Example training data
train_data = torch.rand(1000, 784)  # 1000 samples, each with 784 features
train_labels = torch.randint(0, 10, (1000,))  # 1000 labels (0-9)
train_loader = DataLoader(TensorDataset(train_data, train_labels), batch_size=32, shuffle=True)

# Train the model
for epoch in range(10):
    running_loss = 0.0
    for data, labels in train_loader:
        optimizer.zero_grad()        # Clear gradients
        outputs = model(data)        # Forward pass
        loss = criterion(outputs, labels)  # Compute loss
        loss.backward()              # Backward pass
        optimizer.step()             # Update weights
        running_loss += loss.item()  # Accumulate loss
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")  # Print average loss per epoch
