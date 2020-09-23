import tensorflow as tf 

def adder(a,b):
    return a+ b

a1 = tf.constant([1,2])
a2 = tf.constant([2,4])

print(adder(a1,a2))