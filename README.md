<img src="https://devsar.s3-sa-east-1.amazonaws.com/logo_emails-02.png" alt="Devsar logo" title="Devsar Talks" align="right" height="96" width="96"/>

# Kubernetes examples

This is a basic project with kubernetes examples.

# Tools to run the examples

- <a href="https://minikube.sigs.k8s.io" target="_blank">**Minikube**</a> to run K8s Locally.

- <a href="https://locust.io" target="_blank">**Locust**</a> to stress the cluster.


## Running simple nginx

        kubectl run my-nginx --image=nginx --port=80
        kubectl get pods


## Running NodeJS Deployment

        docker build -t devsar-node:1.0 .
        kubectl create deployment devsar-node --image=devsar-node:1.0
        kubectl get deployments
        kubectl get pods
        kubectl expose deployment devsar-node --type=LoadBalancer --port=8080
        kubectl get services
        minikube service hello-node

## Running simple POD

        kubectl apply -f redis-pod.yaml

## Running older version and update deployment

        kubectl apply -f deployment-nginx-1.14.2.yaml
        kubectl get deployments
        kubectl apply -f deployment-nginx-1.16.1.yaml
        kubectl get deployments

## Running Scaling PODs
        
        kubectl apply -f deployment-nginx-scaling.yaml
        kubectl expose deployment nginx-deployment --type=LoadBalancer --port=80

## Running Auto Scaling Cluster

        minikube addons enable metrics-server
        kubectl apply -f deployment-nginx-autoscaling.yaml      

## Running Stress script
        locust -f stress.py --host http://host:port 

