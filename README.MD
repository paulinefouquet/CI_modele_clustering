# Clustering Evaluation

Projet Sandbox pour tester du CI CD sur Azure
### Continuous Deploiement :

1. Prérequis  
suppression de la version actuelle du groupe du container existant 
paulineContainerGroupB15-2  
2. Obtenir des azure credentials avec un SP  
3. Obtenir le password du registre d'image paulineregistreb15  
4. A chaque push sur main le projet est testé et deployé sur Azure 
5. Une fois que le workflow est OK, rendez-vous sur la page:  
http://pauline-ajax-clustering2.westeurope.azurecontainer.io:8888/