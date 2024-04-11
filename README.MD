# Clustering Evaluation

## Démarrage

### DOCKER / AZURE :

Executer les commandes ci-dessous dans le répertoire backend/  
1. Construction des images  
```
docker build -t back-ajax-az .
docker build -t front-ajax-az .
```
```
docker tag back-ajax-az paulineregistreb15.azurecr.io/pauline-b15-back
docker push paulineregistreb15.azurecr.io/pauline-b15-back
```
```
docker tag front-ajax-az paulineregistreb15.azurecr.io/pauline-b15-front
docker push paulineregistreb15.azurecr.io/pauline-b15-front
```

Executer le groupe de container avec la commande ci-dessous et en remplacant psw par le psw du registre d'image accessible dans accessKey :

```
az container create --resource-group pauline-RG-Brief15 --file deploy-aci.yaml --registry-username paulineregistreb15 --registry-password psw
```

Rendez-vous sur la page http://pauline-ajax-clustering.eastus.azurecontainer.io:8888/