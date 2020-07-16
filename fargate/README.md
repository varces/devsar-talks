<img src="https://devsar.s3-sa-east-1.amazonaws.com/logo_emails-02.png" alt="Devsar logo" title="Devsar Talks" align="right" height="96" width="96"/>

# Fargate EKS examples

This is a basic project with Fargate EKS examples.

# Tools to run the examples

- <a href="https://docs.aws.amazon.com/es_es/eks/latest/userguide/eksctl.html#installing-eksctl" target="_blank">**eksctl**</a> CLI to create a new EKS cluster.
- <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/" target="_blank">**kubectl**</a> CLI to interact with the kubernetes API server.

- <a href="https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-install.html" target="_blank">**AWS CLI**</a> AWS CLI .



## Running fargate

        kubectl run my-nginx --image=nginx --port=80
        kubectl get pods



