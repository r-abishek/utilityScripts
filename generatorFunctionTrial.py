'''
import itertools
import tensorflow as tf
# tf.compat.v1.enable_eager_execution()

def gen():
  for i in itertools.count(1):
    yield (i, [1] * i)

ds = tf.data.Dataset.from_generator(
    gen, (tf.int64, tf.int64), (tf.TensorShape([]), tf.TensorShape([None])))

for value in ds.take(2):
  tf.print(value)
'''



import numpy as np
import tensorflow as tf

numSteps = 10
batchSize = 2

# from generator
def rali_processed_tensors_generator(i):
    # i = 0
    # while True:
    sequence = np.array([
        [[1 + i], [2 + i], [3 + i], [4 + i]],
        [[5 + i], [6 + i], [7 + i], [8 + i]],
        [[9 + i], [10 + i], [11 + i], [12 + i]],
        [[13 + i], [14 + i], [15 + i], [16 + i]],
        [[17 + i], [18 + i], [19 + i], [20 + i]],
        [[21 + i], [22 + i], [23 + i], [24 + i]],
        [[25 + i], [26 + i], [27 + i], [28 + i]]
    ])

    sequence2 = np.array([
        [1 + i],
        [5 + i],
        [9 + i],
        [13 + i],
        [17 + i],
        [21 + i],
        [25 + i]
    ])

        # yield sequence, sequence2
        # i += 100
    return sequence, sequence2

# dict1 = {
#     ""
# }

print("\nOut here")

def generator():
    print("\nIn here")
    # for el in sequence:
    #     print("\nIn here - in loop")
    #     yield el
    # for i in list(range(numSteps)):
    i = 0
    resetCount = 0
    sequence = np.array([])
    sequence2 = np.array([])
    while True:
        
        print("\nIn here - in loop")
        
        testElement = sequence[(i * batchSize) : ((i * batchSize) + batchSize)]
        if testElement.size == 0:
            print("\nSize = 0")
            i = 0
            sequence, sequence2 = rali_processed_tensors_generator(resetCount * 100)
            resetCount += 1
            # sequence = result[0]
            # sequence2 = result[1]

        print (i)
        print(i * batchSize)
        print((i * batchSize) + batchSize)
        yield sequence[(i * batchSize) : ((i * batchSize) + batchSize)], sequence2[(i * batchSize) : ((i * batchSize) + batchSize)]
        i += 1

# 0
# 0:2

# 1
# 2:4

# 2
# 4:6

dataset = tf.data.Dataset.from_generator(generator,
                                           output_types= (tf.int64, tf.int64)
                                        #    output_shapes=(tf.TensorShape([None, 4, 1]), tf.TensorShape([None, 1]))
                                           )

print("\nOut here")
# dataset = dataset.batch(batchSize, drop_remainder=True)
# iter = dataset.make_initializable_iterator()
iter = dataset.make_one_shot_iterator()
el = iter.get_next()
print("\nOut here - done")
with tf.Session() as sess:
    # sess.run(iter.initializer)
    # print(sess.run(el))
    # print(sess.run(el))
    # print(sess.run(el))

    for count in list(range(numSteps)):
        # print(sess.run(el))
        elem1, elem2 = sess.run(el)
        print (elem1)
        print (elem2)



'''
global step  =

'''

