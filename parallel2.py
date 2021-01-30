import numpy as np
from time import time
import multiprocessing as mp

def get_onehot(image_labels_array, numClasses):
	one_hot_vector_list = []
	for label in image_labels_array:
		one_hot_vector = np.zeros(numClasses)
		if label[0] != 0:
			np.put(one_hot_vector, label[0] - 1, 1)
		one_hot_vector_list.append(one_hot_vector)
	one_hot_vector_array = np.array(one_hot_vector_list)

	return one_hot_vector_array

def get_weights(num_bboxes):
	weights_array = np.zeros(100)
	for pos in list(range(num_bboxes)):
		np.put(weights_array, pos, 1)
	
	return weights_array

def get_shapes(image_array):
  
  return len(image_array), len(image_array[0]), len(image_array[0,0])

def get_normalized(image_bboxes, image_height, image_width):
  image_bboxes_normalized = np.empty([0, 4], dtype = np.float32)
  for element in image_bboxes:
    image_bboxes_normalized = np.append(image_bboxes_normalized, np.array([
      [
        element[1] / image_height,
        element[0] / image_width,
        (element[1] + element[3]) / image_height,
        (element[0] + element[2]) / image_width
      ]
    ], dtype = np.float32), axis = 0)
  
  return image_bboxes_normalized

def rali_parallelized_tensor_generator(data_tuple):
    
    image = data_tuple[0]
    bboxes_in_image = data_tuple[1]
    labels_in_image = data_tuple[2]
    num_bboxes_in_image = data_tuple[3]
    unique_key_for_image = data_tuple[4]
    numClasses = data_tuple[5]

    hash_key_tensor = str(unique_key_for_image)
    images_tensor = image
    num_groundtruth_boxes_tensor = num_bboxes_in_image
    true_image_shapes_tensor = get_shapes(image)
    groundtruth_boxes_tensor = get_normalized(bboxes_in_image, len(image), len(image[0]))
    groundtruth_classes_tensor = get_onehot(labels_in_image, numClasses)
    groundtruth_weights_tensor = get_weights(num_bboxes_in_image)

    return [hash_key_tensor, 
    images_tensor, 
    num_groundtruth_boxes_tensor, 
    true_image_shapes_tensor, 
    groundtruth_boxes_tensor, 
    groundtruth_classes_tensor, 
    groundtruth_weights_tensor]

def main():
    batch_size = 8
    numClasses = 90

    images_array = np.random.randint(0, 255, size=[batch_size, 320, 320, 3]).astype(np.float32)
    bboxes_array = np.random.randint(0, 320, size=[batch_size, 100, 4]).astype(np.float32)
    labels_array = np.random.randint(0, 10, size=[batch_size, 100, 1])
    num_bboxes_array = np.random.randint(0, 100, size=[batch_size])

    






    # PARALLEL CODE
    # '''
    result = []
    hash_key_tensor = []
    images_tensor = []
    num_groundtruth_boxes_tensor = []
    true_image_shapes_tensor = []
    groundtruth_boxes_tensor = []
    groundtruth_classes_tensor = []
    groundtruth_weights_tensor = []
    
    pool = mp.Pool(mp.cpu_count())
    sourceID = 1000000
    
    start_time_parallel = time()

    for batch_num in list(range(2)):
        
        result = pool.map(rali_parallelized_tensor_generator, np.array([
            [images_array[i], bboxes_array[i], labels_array[i], num_bboxes_array[i], sourceID + i, numClasses] for i in list(range(batch_size))
            ]))

        for image_data in result:
            hash_key_tensor.append(image_data[0])
            images_tensor.append(image_data[1])
            num_groundtruth_boxes_tensor.append(image_data[2])
            true_image_shapes_tensor.append(image_data[3])
            groundtruth_boxes_tensor.append(image_data[4])
            groundtruth_classes_tensor.append(image_data[5])
            groundtruth_weights_tensor.append(image_data[6])
        
        sourceID += batch_size
    
    end_time_parallel = time()

    pool.close()

    # print("\n\n\nPARALLEL CODE OUTPUT:")
    # print("hash_key_tensor:\n", hash_key_tensor)
    # print("images_tensor:\n", images_tensor)
    # print("num_groundtruth_boxes_tensor:\n", num_groundtruth_boxes_tensor)
    # print("true_image_shapes_tensor:\n", true_image_shapes_tensor)
    # print("groundtruth_boxes_tensor:\n", groundtruth_boxes_tensor)
    # print("groundtruth_classes_tensor:\n", groundtruth_classes_tensor)
    # print("groundtruth_weights_tensor:\n", groundtruth_weights_tensor)
    # '''
    




    # SERIAL CODE
    # '''
    hash_key_tensor = []
    images_tensor = np.empty([0, 320, 320, 3], dtype = np.float32)
    true_image_shapes_tensor = np.empty([0, 3], dtype = np.int32)
    num_groundtruth_boxes_tensor = np.empty([0], dtype = np.int32)
    groundtruth_boxes_tensor = np.empty([0, 100, 4], dtype = np.float32)
    groundtruth_classes_tensor = np.empty([0, 100, numClasses], dtype = np.float32)
    groundtruth_weights_tensor = np.empty([0, 100], dtype = np.float32)
    
    sourceID = 1000000
    
    start_time_serial = time()
    
    for batch_num in list(range(2)):
        
        for element in list(range(batch_size)):
            hash_key_tensor.append(str(sourceID))
            images_tensor = np.append(images_tensor, np.array([images_array[element]], dtype = np.float32), axis = 0)
            num_groundtruth_boxes_tensor = np.append(num_groundtruth_boxes_tensor, np.array([num_bboxes_array[element]], dtype = np.int32), axis = 0)
            true_image_shapes_tensor = np.append(true_image_shapes_tensor, np.array([get_shapes(images_array[element])], dtype = np.int32), axis = 0)
            groundtruth_boxes_tensor = np.append(groundtruth_boxes_tensor, np.array([get_normalized(bboxes_array[element], len(images_array[element]), len(images_array[element,0]))], dtype = np.float32), axis = 0)
            groundtruth_classes_tensor = np.append(groundtruth_classes_tensor, np.array([get_onehot(labels_array[element], numClasses)], dtype = np.float32), axis = 0)
            groundtruth_weights_tensor = np.append(groundtruth_weights_tensor, np.array([get_weights(num_bboxes_array[element])], dtype = np.float32), axis = 0)
            sourceID += 1
    
    end_time_serial = time()


    # print("\n\n\nSERIAL CODE OUTPUT:")
    # print("hash_key_tensor:\n", hash_key_tensor)
    # print("images_tensor:\n", images_tensor)
    # print("num_groundtruth_boxes_tensor:\n", num_groundtruth_boxes_tensor)
    # print("true_image_shapes_tensor:\n", true_image_shapes_tensor)
    # print("groundtruth_boxes_tensor:\n", groundtruth_boxes_tensor)
    # print("groundtruth_classes_tensor:\n", groundtruth_classes_tensor)
    # print("groundtruth_weights_tensor:\n", groundtruth_weights_tensor)
    # '''
    
    
    print("--- %s seconds ---" % (end_time_parallel - start_time_parallel))
    print("--- %s seconds ---" % (end_time_serial - start_time_serial))


if __name__ == "__main__":
    main()





# Solution Without Paralleization
'''
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    
    # trial = 0
    # for i in list(range(5000)):
    #     trial += 1
    return count

# results = []
results = np.empty([0], dtype = np.int32)
start_time = time()
for row in data:
    # results.append(howmany_within_range(row, minimum=320, maximum=320))
    results = np.append(results, np.array([howmany_within_range(row, minimum=320, maximum=320)]))

end_time = time()

print(results)
print("--- %s seconds ---" % (end_time - start_time))
'''



# Parallelizing using Pool.apply()
'''
import multiprocessing as mp

# Step 1: Init multiprocessing.Pool()
# pool = mp.Pool(mp.cpu_count())
pool = mp.Pool(10)

# Step 2: `pool.apply` the `howmany_within_range()`
results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

# Step 3: Don't forget to close
pool.close()    

print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
'''



# Parallelizing using Pool.map()
'''
import multiprocessing as mp

# Redefine, with only 1 mandatory argument.
def howmany_within_range_rowonly(row, minimum=320, maximum=320):
    print(row)
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    
    # trial = 0
    # for i in list(range(5000)):
    #     trial += 1
    
    return count

pool = mp.Pool(mp.cpu_count())
# pool = mp.Pool(10)

start_time = time()
results = pool.map(howmany_within_range_rowonly, np.array([row for row in data]))
end_time = time()

pool.close()

results = np.array(results)

print(results)
print("--- %s seconds ---" % (end_time - start_time))
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
'''


