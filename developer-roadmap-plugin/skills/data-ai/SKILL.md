---
name: data-ai-technologies
description: Master data science and AI with machine learning, deep learning, and LLMs. Use when building ML models, working with data, or implementing AI features.
---

# Data Science & AI Technologies Skill

Comprehensive guide to data science and AI development.

## Quick Start

### Python Data Analysis
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Data exploration
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Data cleaning
df = df.dropna()
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Grouping and aggregation
summary = df.groupby('category')['sales'].agg(['mean', 'sum', 'count'])

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()
```

### Machine Learning with scikit-learn
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")
```

### Deep Learning with PyTorch
```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):
    for batch_x, batch_y in train_loader:
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### Using LLMs
```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain machine learning in simple terms."}
    ],
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].message.content)
```

## Key Concepts

### Data Processing
- Data cleaning and preprocessing
- Feature engineering
- Data normalization and scaling
- Handling missing values
- Outlier detection
- Dimensionality reduction

### Machine Learning
- Supervised vs unsupervised learning
- Classification and regression
- Hyperparameter tuning
- Cross-validation
- Overfitting prevention
- Model selection

### Deep Learning
- Neural network architecture
- Activation functions
- Backpropagation
- Convolutional networks (CNN)
- Recurrent networks (RNN, LSTM)
- Transfer learning
- Fine-tuning pre-trained models

### Large Language Models
- Transformer architecture
- Tokenization
- Embeddings
- Prompt engineering
- RAG (Retrieval Augmented Generation)
- Fine-tuning LLMs
- Cost optimization

### Evaluation Metrics
- Accuracy, Precision, Recall, F1
- ROC-AUC curve
- Confusion matrix
- Mean squared error (MSE)
- Mean absolute error (MAE)
- Perplexity for language models

## Popular Libraries

### Data Processing
- Pandas: Data manipulation
- NumPy: Numerical computing
- Polars: Fast data processing
- DuckDB: SQL for data analysis

### Machine Learning
- scikit-learn: Classical ML
- XGBoost: Gradient boosting
- LightGBM: Fast boosting
- CatBoost: Categorical boosting

### Deep Learning
- PyTorch: Flexible framework
- TensorFlow: Production framework
- JAX: Numerical computing
- Hugging Face: Transformers library

### Data Visualization
- Matplotlib: Static plots
- Seaborn: Statistical visualizations
- Plotly: Interactive plots
- Altair: Declarative visualization

## Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Hugging Face Course](https://huggingface.co/course/)
- [Fast.ai Courses](https://course.fast.ai/)
- [Kaggle Datasets](https://www.kaggle.com/datasets/)
