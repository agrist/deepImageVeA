npm install node
npm install express
npm install shelljs
npm install fs

sudo python retrain.py --how_many_training_steps 4000 --output_labels=/bottlenecks/retrained_labels.txt --output_graph=/bottlenecks/retrained_graph.pb

change the paths in image_check.py

node server.js