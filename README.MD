# Clustering Evaluation

## Démarrage

### DOCKER / AZURE :

Executer les commandes ci-dessous dans le répertoire backend/  
1. Construction des images  
```
docker build -t back-ajax2-az .
```
Executer les commandes ci-dessous dans le répertoire frontend/  
```
docker build -t front-ajax2-az .
```

```
docker tag back-ajax2-az paulineregistreb15.azurecr.io/pauline-b15-back2
```
```
docker tag front-ajax2-az paulineregistreb15.azurecr.io/pauline-b15-front2
```


pour les commandes ci-dessous au préalable se connecter à azure et au registre
```
az login
az acr login --name paulineregistreb15
```

```
docker push paulineregistreb15.azurecr.io/pauline-b15-back2
```
```
docker push paulineregistreb15.azurecr.io/pauline-b15-front2
```

Executer le groupe de container avec la commande ci-dessous à la racine du projet:

```
az container create --resource-group pauline-RG-Brief15 --file deploy-aci.yaml --registry-username paulineregistreb15
```

Rendez-vous sur la page http://pauline-ajax-clustering2.westeurope.azurecontainer.io:8888/