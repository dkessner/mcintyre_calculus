import numpy as np


def predict(x, w, b):
    """Makes a prediction with a linear model."""
    y_hat = w * x + b
    return y_hat


def backprop(x, y, y_hat):
    """Computes the error gradient."""
    m = len(x)
    dE_dw = (1 / m) * np.sum((y_hat - y) * x)
    dE_db = (1 / m) * np.sum(y_hat - y)
    return dE_dw, dE_db


def train(x, y, num_epochs=100000, alpha=0.00001):
    """Trains a neuron with backpropagation and gradient descent."""
    w = np.random.random() - 0.5
    b = np.random.random() - 0.5
    for i in range(num_epochs):
        # Make a prediction.
        y_hat = predict(x, w, b)
        # Compute the error gradient.
        dE_dw, dE_db = backprop(x, y, y_hat)
        # Descend the gradient.
        w -= alpha * dE_dw
        b -= alpha * dE_db
    return w, b


def r_squared(y, y_hat):
    """Computes the coefficient of determination."""
    m = len(y)
    y_mean = (1 / m) * np.sum(y)
    RSS = np.sum((y_hat - y) ** 2)
    TSS = np.sum((y - y_mean) ** 2)
    R2 = 1 - RSS / TSS
    return R2


def predict_mlr(x, w, b):
    y_hat = w @ x + b
    return y_hat


def train_mlr(X, y, num_epochs=100000, alpha=0.00001):
    """Trains a neuron with backpropagation and gradient descent."""
    n = X.shape[0]
    w = np.random.random(n) - 0.5
    b = np.random.random() - 0.5
    for i in range(num_epochs):
        # Make a prediction.
        x = X[:, i]
        y_hat = predict_mlr(x, w, b)
        # Compute the error gradient.
        dE_dw, dE_db = backprop(x, y, y_hat)
        # Descend the gradient.
        w -= alpha * dE_dw
        b -= alpha * dE_db
    return w, b