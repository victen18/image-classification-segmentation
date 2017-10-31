"""
"""
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import UpSampling2D

def fcn8():
    
    x = Sequential()
    
    # Block 1
    x.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu', padding='same', name='block1_conv1'))
    x.add(Conv2D(32, (3, 3), activation='relu', padding='same', name='block1_conv2'))
    x.add(MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool'))
    x.add(Dropout(0.5))

    # Block 2
    x.add(Conv2D(64, (3, 3), activation='relu', padding='same', name='block2_conv1'))
    x.add(Conv2D(64, (3, 3), activation='relu', padding='same', name='block2_conv2'))
    x.add(MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool'))
    x.add(Dropout(0.5))
    
    # Block 3
    x.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block3_conv1'))
    x.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block3_conv2'))
    x.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block3_conv3'))
    x.add(MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool'))
    x.add(Dropout(0.5))
    
    # Continue to use convolutional layers instead of dense layers in cnn10
    x.add(Conv2D(256, (4, 4), activation='relu', padding='same', name='fcn1'))
    x.add(Dropout(0.5))
    x.add(Conv2D(256, (1, 1), activation='relu', padding='same', name='fcn2'))
    x.add(Dropout(0.5))
    # write a BilinearUpSampling2D layer
    
    return x
