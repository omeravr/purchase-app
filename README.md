# Purchase App

This repository contains the code and deployment configurations for the Purchase App application.

## Overview

The Purchase App is a distributed application consisting of multiple components deployed on a Kubernetes cluster. Each component serves a specific purpose within the application ecosystem.

## Components

- **API Server**: This component provides APIs for managing customers.
- **Kafka**: Apache Kafka is used as a messaging system to handle asynchronous communication between components.
- **MongoDB**: MongoDB is used as the database for storing customer data.
- **Web Server**: The customer-facing web server serves the user interface for interacting with the application.
- **my-app-chart**: The folder used to package the chart and upload it to https://github.com/omeravr/purchase-app-chart.git

## Folder Structure

The repository is organized into directories corresponding to each component:

- `api-server`: Contains code and deployment configurations for the API server.
- `kafka`: Contains deployment configurations for Apache Kafka.
- `mongo`: Contains deployment configurations for MongoDB.
- `web-server`: Contains code and deployment configurations for the web server.

## Deployment

To deploy the Purchase App application on a Kubernetes cluster, follow these steps:

1. Ensure you have Helm installed on your system.
2. Add the Helm repository:
   ```bash```
   helm repo add my-repo https://omeravr.github.io/purchase-app-chart/
3. Install the chart:
	helm install my-release my-repo/my-app-chart

## Accessing the Application:

Once the chart is installed, you can access the application using the NodePort service created for the customer-facing-webserver.

To get the NodePort and the IP address of your Kubernetes node, you can use the following commands:
kubectl get nodes -o wide
and:
kubectl get svc -n default customer-facing-webserver

The output will contain the NodePort and the External-IP of your nodes. Use the External-IP and the NodePort to access the application.

For example, if the External-IP is 10.20.30.40 and the NodePort is 31000, you can access the application at:
http://10.20.30.40:31000/



## Uninstalling the Chart:

To uninstall the chart, you can use the following command:
bash
Copy code
helm uninstall my-release
