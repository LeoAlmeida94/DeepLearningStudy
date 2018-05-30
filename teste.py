import numpy as np
np.random.seed(123)  # for reproducibility

#modelo sequencal do keras, em que eh uma simples pilha linear de camadas de rede neural
from keras.models import Sequential
#camadas que serao ser usadas na rede
from keras.layers import Dense, Dropout, Activation, Flatten
#Camadas convolucionais
from keras.layers import Convolution2D, MaxPooling2D

from keras.utils import np_utils

#Load MNIST data
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print X_train.shape
