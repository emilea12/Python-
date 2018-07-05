import tensorflow as tf


# Create a tensor representing a blank image
batch = tf.zeros([1, 1, 784])
print(batch.shape)  # => (1, 1, 784)

result = model(batch)
# => tf.Tensor([[[ 0.  0., ..., 0.]]], shape=(1, 1, 10), dtype=float32)