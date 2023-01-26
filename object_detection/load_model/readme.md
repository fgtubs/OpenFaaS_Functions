# Read in the tensorflow model

faas deploy --image anyfin/tensorflow-hub-model-test:v0.0.1 --name tensorflow-hub-model-test --fprocess "python index.py" -d "https://upload.wikimedia.org/wikipedia/commons/6/60/Naxos_Taverna.jpg"
