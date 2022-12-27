# UdaConnect-Refactored-into-Microservices
UdaConnect is Project #2 of Udacity's Cloud Native Application Architecture Nanodegree. This is my solution for this project.

## Dependencies
These technologies are used in this project:
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - API webserver
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
* [PostgreSQL](https://www.postgresql.org/) - Relational database
* [PostGIS](https://postgis.net/) - Spatial plug-in for PostgreSQL enabling geographic queries]
* [Vagrant](https://www.vagrantup.com/) - Tool for managing virtual deployed environments
* [VirtualBox](https://www.virtualbox.org/) - Hypervisor allowing you to run multiple operating systems
* [K3s](https://k3s.io/) - Lightweight distribution of K8s to easily develop against a local cluster
* [Helm](https://helm.sh/docs/intro/install/) - A package manager for Kubernetes

## Prerequisites for Running Locally
These tools are necessary for getting a (local, virtual) environment set up properly.
1. [Install Docker](https://docs.docker.com/get-docker/)
2. [Set up a DockerHub account](https://hub.docker.com/)
3. [Set up `kubectl`](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/cluster-access/kubectl/)
4. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads) with at least version 6.0
5. [Install Vagrant](https://www.vagrantup.com/docs/installation) with at least version 2.0

## Deployment: Environment Setup
To run the application, you will need a K8s cluster running locally and to interface with it via `kubectl`. In this project Vagrant with VirtualBox is used to run K3s.

### Initialize K3s
In this project's root, run `vagrant up`.
```bash
$ vagrant up
```
The command will take a while and will leverage VirtualBox to load an [openSUSE](https://www.opensuse.org/) OS and automatically install [K3s](https://k3s.io/). When we are taking a break from development, we can run `vagrant suspend` to conserve some ouf our system's resources and `vagrant resume` when we want to bring our resources back up. Some useful vagrant commands can be found in [this cheatsheet](https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4).

### Deploy Helm

### Deploy Zookeeper and Kafka

### Deploy Utilities: Vim, Git

#### Set up `kubectl` to Interact with the Cluster
After `vagrant up` is done, you will SSH into the Vagrant environment and retrieve the Kubernetes config file used by `kubectl`. We want to copy the contents of this file into our local environment so that `kubectl` knows how to communicate with the K3s cluster.
```bash
$ vagrant ssh
```
You will now be connected inside of the virtual OS. Run `sudo cat /etc/rancher/k3s/k3s.yaml` to print out the contents of the file. You should see output similar to the one that I've shown below. Note that the output below is just for your reference: every configuration is unique and you should _NOT_ copy the output I have below.

Copy the contents from the output issued from your own command into your clipboard -- we will be pasting it somewhere soon!
```bash
$ sudo cat /etc/rancher/k3s/k3s.yaml

apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUJWekNCL3FBREFnRUNBZ0VBTUFvR0NDcUdTTTQ5QkFNQ01DTXhJVEFmQmdOVkJBTU1HR3N6Y3kxelpYSjIKWlhJdFkyRkFNVFU1T1RrNE9EYzFNekFlRncweU1EQTVNVE13T1RFNU1UTmFGdzB6TURBNU1URXdPVEU1TVROYQpNQ014SVRBZkJnTlZCQU1NR0dzemN5MXpaWEoyWlhJdFkyRkFNVFU1T1RrNE9EYzFNekJaTUJNR0J5cUdTTTQ5CkFnRUdDQ3FHU000OUF3RUhBMElBQk9rc2IvV1FEVVVXczJacUlJWlF4alN2MHFseE9rZXdvRWdBMGtSN2gzZHEKUzFhRjN3L3pnZ0FNNEZNOU1jbFBSMW1sNXZINUVsZUFOV0VTQWRZUnhJeWpJekFoTUE0R0ExVWREd0VCL3dRRQpBd0lDcERBUEJnTlZIUk1CQWY4RUJUQURBUUgvTUFvR0NDcUdTTTQ5QkFNQ0EwZ0FNRVVDSVFERjczbWZ4YXBwCmZNS2RnMTF1dCswd3BXcWQvMk5pWE9HL0RvZUo0SnpOYlFJZ1JPcnlvRXMrMnFKUkZ5WC8xQmIydnoyZXpwOHkKZ1dKMkxNYUxrMGJzNXcwPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    server: https://127.0.0.1:6443
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
kind: Config
preferences: {}
users:
- name: default
  user:
    password: 485084ed2cc05d84494d5893160836c9
    username: admin
```
Type `exit` to exit the virtual OS and you will find yourself back in your computer's session. Create the file (or replace if it already exists) `~/.kube/config` and paste the contents of the `k3s.yaml` output here.

Afterwards, you can test that `kubectl` works by running a command like `kubectl describe services`. It should not return any errors.

## Deployment: Application Deployment

## Architecture Overview

## The Microservice "locationfeeder"
The state of this container is
[![locationfeeder - build and push to DockerHub](https://github.com/StephanStu/UdaConnect-Refactored-into-Microservices/actions/workflows/build_and_push_locationfeeder.yaml/badge.svg)](https://github.com/StephanStu/UdaConnect-Refactored-into-Microservices/actions/workflows/build_and_push_locationfeeder.yaml)

## The Microservice "frontend"
The state of this container is [![frontend - build and push to DockerHub](https://github.com/StephanStu/UdaConnect-Refactored-into-Microservices/actions/workflows/build_and_push_frontend.yaml/badge.svg)](https://github.com/StephanStu/UdaConnect-Refactored-into-Microservices/actions/workflows/build_and_push_frontend.yaml)

### Steps
1. `kubectl apply -f deployment/db-configmap.yaml` - Set up environment variables for the pods
2. `kubectl apply -f deployment/db-secret.yaml` - Set up secrets for the pods
3. `kubectl apply -f deployment/postgres.yaml` - Set up a Postgres database running PostGIS
4. `kubectl apply -f deployment/udaconnect-api.yaml` - Set up the service and deployment for the API
5. `kubectl apply -f deployment/udaconnect-app.yaml` - Set up the service and deployment for the web app
6. `sh scripts/run_db_command.sh <POD_NAME>` - Seed your database against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`)

Manually applying each of the individual `yaml` files is cumbersome but going through each step provides some context on the content of the starter project. In practice, we would have reduced the number of steps by running the command against a directory to apply of the contents: `kubectl apply -f deployment/`.

Note: The first time you run this project, you will need to seed the database with dummy data. Use the command `sh scripts/run_db_command.sh <POD_NAME>` against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`). Subsequent runs of `kubectl apply` for making changes to deployments or services shouldn't require you to seed the database again!

### Verifying it Works
Once the project is up and running, you should be able to see 3 deployments and 3 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return `udaconnect-app`, `udaconnect-api`, and `postgres`


These pages should also load on your web browser:
* `http://localhost:30001/` - OpenAPI Documentation
* `http://localhost:30001/api/` - Base path for API
* `http://localhost:30000/` - Frontend ReactJS Application

#### Deployment Note
You may notice the odd port numbers being served to `localhost`. [By default, Kubernetes services are only exposed to one another in an internal network](https://kubernetes.io/docs/concepts/services-networking/service/). This means that `udaconnect-app` and `udaconnect-api` can talk to one another. For us to connect to the cluster as an "outsider", we need to a way to expose these services to `localhost`.

Connections to the Kubernetes services have been set up through a [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport). (While we would use a technology like an [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to expose our Kubernetes services in deployment, a NodePort will suffice for development.)

#### Useful Commands
This section list some commands that showed to be worth keeping in mind.
* ssh into a pod that is in a namespace

```bash
$ kubectl exec -it [pod-name] -n [namespace-name] -- /bin/bash
```

* Export the kube-config to where it is expected to avoid [this](https://github.com/k3s-io/k3s/issues/1126) error.

```bash
$ kubectl config view --raw >~/.kube/config
```

* A simple Kafka-Client that you can use for testing

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kafka-client
spec:
  containers:
  - name: kafka-client
    image: docker.io/bitnami/kafka:2.8.0-debian-10-r43
    # Just sleep forever
    command: [ "sleep" ]
    args: [ "infinity" ]
```

Create this as *kafka-client.yaml* and then

```bash
$ kubectl apply -f kafka-client.yaml
```

Wait until all pods have reached the state RUNNING, then

```bash
$ kubectl exec --tty -i kafka-client --namespace default -- bash
```

Once on the client create a topic and post some stuff by

```bash
kafka-console-producer.sh --broker-list kafkacluster-0.kafkacluster-headless.default.svc.cluster.local:9092 --topic test
```

Consume your stuff by

```bash
kafka-console-consumer.sh --bootstrap-server kafkacluster.default.svc.cluster.local:9092 --topic test --from-beginning
```
