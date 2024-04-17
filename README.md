# Clustering Evaluation

Projet Sandbox pour tester du CI CD sur Azure  

## Continuous Deploiement :

1. Obtenir un Service Principal auprès d'un owner de la subscription Azure  

2. Obtenir le password du registre d'image paulineregistreb15  

3. Definir les Github Secrets :  
AZURE_CREDENTIALS  
IMAGE_REGISTRY_PASSWORD   

4. A chaque push sur main le projet est testé et deployé sur Azure 

5. Rendez-vous sur la page:  
http://pauline-ajax-clustering2.westeurope.azurecontainer.io:8888/