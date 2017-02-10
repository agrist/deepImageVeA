import tensorflow as tf, sys
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
#from additionalFunctions import additionalFunctions
#af=additionalFunctions()
# change this as you see fit
image_path = 'C:\\Users\\PCD306\\Desktop\\OrthoProcessing\\NeuralNetwork\\TestImages\\LiepajaSmall.jpg'
im=misc.imread(image_path)
print(im.shape)

r=im.shape[0]
k=im.shape[1]
print(r)
print(k)
images_placeholder=tf.placeholder(tf.int32)
# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("C:\\tmp\\output_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("C:\\tmp\\output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

result=np.zeros((r,k))
buf=40
step=40;
for i in range(0,r-(step+1),step):
	print("Row")
	print(i)
	for j in range(0,k-(step+1),step):
		rstart=i-buf;
		rend=i+buf;
		kstart=j-buf;
		kend=j+buf;
		if rstart<0:
			rstart=0
		if rend>r-1:
			rend=r-1
		if kstart<0:
			kstart=0
		if kend>k-1:
			kend=k-1
		ims=im[rstart:rend,kstart:kend];
		with tf.Session() as sess:
			# Feed the image_data as input to the graph and get first prediction
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
			predictions = sess.run(softmax_tensor,{'DecodeJpeg:0': ims})
			print("Prognozes")
			print(predictions[0,1])
			result[i,j]=predictions[0,1]
			result[i,j+1:j+step-1]=predictions[0,1]
			result[i+1:i+step-1, j+1:j+step-1]=predictions[0,1]
#misc.imsave('result.tif',result)
print(result)
plt.imsave('result5MazasMajas.png',result,vmin=0,vmax=1,format='png')
