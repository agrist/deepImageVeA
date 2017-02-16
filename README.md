install node and npm if needed, then in the folder:

npm install node
^(this should create and download all dependencies, if not continue with the npm install statements below)

npm install express
npm install shelljs
npm install fs
npm install multer
npm install body-parser

sudo python retrain.py --how_many_training_steps 4000 --output_labels=/bottlenecks/retrained_labels.txt --output_graph=/bottlenecks/retrained_graph.pb --bottleneck_dir=/bottlenecks


(change the paths in image_check.py if needed )

node server.js
go to http://127.0.0.1:8090

