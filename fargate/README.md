<img src="https://devsar.s3-sa-east-1.amazonaws.com/logo_emails-02.png" alt="Devsar logo" title="Devsar Talks" align="right" height="96" width="96"/>

# Fargate EKS examples

This is a basic project with Fargate EKS examples.

# Tools to run the examples

- <a href="https://docs.aws.amazon.com/es_es/eks/latest/userguide/eksctl.html#installing-eksctl" target="_blank">**eksctl**</a> CLI to create a new EKS cluster.
- <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/" target="_blank">**kubectl**</a> CLI to interact with the kubernetes API server.

- <a href="https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-install.html" target="_blank">**AWS CLI**</a> AWS CLI .



## Create fargate EKS Cluster

- eksctl create cluster --name devsar-cluster-fargate --version 1.16 --fargate

Al añadir la opción --fargate al comando anterior se crea un clúster sin un grupo de nodos. 

## Get VPC ID

- eksctl get cluster --region us-east-2 --name devsar-cluster-fargate -o yaml

## Setup ALB Ingress Controller

- wget https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/rbac-role.yaml
- wget https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/alb-ingress-controller.yaml

Update cluster-name, vpc-id, aws-region, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in alb-ingress-controller.yaml file.


## Deploy to Fargate

- eksctl create fargateprofile --namespace python-api --cluster devsar-cluster-fargate --region us-east-2

## Create Namespace

- kubectl apply -f namespace.yaml

## Create Service

- kubectl apply -f service.yaml


## Create Deployment

- kubectl apply -f deployment.yaml


## Create Ingress

- kubectl apply -f ingress.yaml

## Get Address
kubectl describe ing -n python-api python-api

## Delete Cluster
eksctl delete cluster --region=us-east-2 --name devsar-cluster-fargate




