import sys

print("Hello")
print(sys.version)

import tensorflow as tf
print("Hello")
print(sys.version)


print(tf.config.list_physical_devices("GPU"))
import transformers
import torch
print(tf.keras.__version__)
print(tf.__version__)
print(transformers.__version__)
print(torch.__version__)