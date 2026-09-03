# ==========================================================
# TENSORS IN MACHINE LEARNING
# ==========================================================

# Tensor:
# A numerical data structure used extensively in
# Machine Learning and Deep Learning.

# Tensor can represent:
# Scalar -> 0D
# Vector -> 1D
# Matrix -> 2D
# Higher-dimensional data -> 3D, 4D, 5D, etc.


# -------------------------
# 0D - SCALAR
# -------------------------

# Example:
# 5

# Shape:
# ()


# -------------------------
# 1D - VECTOR
# -------------------------

# Example:
# [1, 2, 3, 4]

# Shape:
# (4,)


# -------------------------
# 2D - MATRIX
# -------------------------

# Example:
# [[1, 2, 3],
#  [4, 5, 6]]

# Shape:
# (2, 3)


# -------------------------
# 3D TENSOR
# -------------------------

# Collection/stack of matrices.

# Example shape:
# (2, 2, 2)


# -------------------------
# 4D TENSOR
# -------------------------

# Commonly used for batches of images.

# PyTorch commonly uses:
# (Batch, Channels, Height, Width)

# Example:
# (32, 3, 224, 224)

# 32  -> Batch size
# 3   -> RGB channels
# 224 -> Height
# 224 -> Width


# -------------------------
# PYTORCH TENSOR
# -------------------------

import torch

x = torch.tensor([1, 2, 3])

# Shape
print(x.shape)

# Number of dimensions
print(x.ndim)

# Data type
print(x.dtype)

# Device
print(x.device)


# -------------------------
# COMMON FUNCTIONS
# -------------------------

# torch.zeros()
# Creates tensor filled with zeros.

# torch.ones()
# Creates tensor filled with ones.

# torch.rand()
# Creates tensor with random values.

# torch.arange()
# Creates sequence of values.


# -------------------------
# TENSOR OPERATIONS
# -------------------------

# a + b -> Element-wise addition
# a - b -> Element-wise subtraction
# a * b -> Element-wise multiplication
# a @ b -> Matrix multiplication


# -------------------------
# RESHAPING
# -------------------------

# reshape() changes the shape while
# keeping the same number of elements.

# unsqueeze() -> Adds a dimension
# squeeze()   -> Removes dimensions of size 1


# -------------------------
# DEVICE
# -------------------------

# Tensors can run on CPU or compatible accelerators.

# x.to("cuda")
# Moves tensor to CUDA device when available.


# -------------------------
# AUTOGRAD
# -------------------------

# PyTorch can automatically calculate gradients.

# Example:
# x = torch.tensor(2.0, requires_grad=True)
# y = x ** 2
# y.backward()
# print(x.grad)


# -------------------------
# GENAI / LLM
# -------------------------

# Text
#   ↓
# Tokenizer
#   ↓
# Token IDs
#   ↓
# Tensor
#   ↓
# Embeddings
#   ↓
# Transformer
#   ↓
# Output Tensor / Logits
#   ↓
# Next Token


# IMPORTANT:
# Tensor = Numerical representation used by
# neural networks for computation.