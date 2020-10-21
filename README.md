# Vmware
how to run the python app on k8s?
first we need to use docker to Containerize the application using docker
step 1: create Dockerfile
step 2: create the image with docker build and check that it exits with docker image ls
step 3: verify its working with docker run
check k8s version with "kubectl version"
If you don’t see a reply with a Client and Server version, you’ll need to install and configure it.
ou can see the node by typing:

kubectl get nodes

Create a file named deployment.yaml:
---
apiVersion: v1
kind: Service
metadata:
  name: python-service
spec:
  selector:
    app: python
  ports:
  - protocol: "TCP"
    port: 80
    targetPort: 5000
  type: http
---
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python
spec:
  selector:
    matchLabels:
      app: python
  replicas: 4
  template:
    metadata:
      labels:
        app: python
    spec:
      containers:
      - name: python
        image: python:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 5000
---
This YAML file is the instructions to Kubernetes for what you want running. It is telling Kubernetes the following:

You want an http service exposing port 80
You want four instances of the app container running

Use kubectl to send the YAML file to Kubernetes by running the following command:

kubectl apply -f deployment.yaml
You can see the pods are running if you execute the following command:

kubectl get pods
